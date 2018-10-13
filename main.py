from google.cloud import datastore
from urllib import quote
import config
import datetime
import google.appengine.api.memcache as memcache
import jinja2
import logging
import os
import random
import webapp2
import xsrfutil


def get_template_vars(self):
  debug = bool(self.request.get('debug') == 'true')
  signed = bool(self.request.cookies.get('signed') == 'true')
  if self.request.get('dev') == 'true':
    signed = False

  # Count
  try:
    count = memcache.get('count')
    if not count:
      client = datastore.Client(config.PROJECT_ID)
      query = client.query(kind='Signature')
      query.keys_only()
      count = len(list(query.fetch()))
      memcache.set('count', count, time=3600)
  except:
    count = 0

  # Neighborhood list count
  try:
    neighborhood_list = memcache.get('neighborhood_list')

    if not neighborhood_list:
      client = datastore.Client(config.PROJECT_ID)
      query = client.query(kind='Signature', projection=['neighborhood'])

      neighborhood_dict = {}
      for item in list(query.fetch()):
        if item['neighborhood'] not in neighborhood_dict:
          neighborhood_dict[item['neighborhood']] = 1
        else:
          neighborhood_dict[item['neighborhood']] += 1

      neighborhood_list = []
      for key, value in neighborhood_dict.iteritems():
        neighborhood_list.append({'name': key, 'count': value})

      memcache.set('neighborhood_list', neighborhood_list, time=3600)

  except:
     neighborhood_list = []

  # Email campaigns
  letter_campaign_active = config.LETTER_CAMPAIGN_ACTIVE or debug

  subject = random.choice(config.EMAIL_SUBJECTS)
  body = random.choice(config.EMAIL_BODYS)

  intro = random.choice(config.EMAIL_OPEN)
  if intro:
    body = intro + '\n\n' + body

  closing = random.choice(config.EMAIL_CLOSE)
  if closing:
    body = body + '\n\n' + closing

  if not debug:
    full_name = self.request.get('full_name')
    neighborhood = self.request.get('neighborhood')
  else:
    full_name = '<< test name >>'
    neighborhood = '<< test neighborhood >>'

  if full_name and neighborhood:
    body = body + '\n\n' + full_name + '\n' + neighborhood + ' resident'

  link = "mailto:%s?subject=%s&body=%s" % (config.RECIPIENTS, quote(subject), quote(body))

  body = body.replace('\n', '<br>')

  # Currently all pages get all template variables
  return {
    'signed': signed,
    'count': count,
    'neighborhood_list': neighborhood_list,
    'neighborhoods': config.NEIGHBORHOODS,
    'letter_campaign_active': letter_campaign_active,
    'letter': {
      'link': link,
      'recipients': config.RECIPIENTS,
      'subject': subject,
      'body': body,
    },
    'app': {
      'current_version_id': os.environ['CURRENT_VERSION_ID'],
    },
    'debug': debug
  }

def get_primary_district(neighborhood_name):
  for neighborhood in config.NEIGHBORHOODS:
    if neighborhood['name'] == neighborhood_name and 'primary_district' in neighborhood:
      return neighborhood['primary_district']
  return ''


class MainPage(webapp2.RequestHandler):
  def get(self):
    # Redirects
    if self.request.path in config.REDIRECTS:
      self.redirect(config.REDIRECTS[self.request.path])

    # Rendered template
    elif self.request.path in config.PAGES:
      template_values = get_template_vars(self)
      template = config.JINJA_ENVIRONMENT.get_template('templates/' + config.PAGES[self.request.path])
      self.response.write(template.render(template_values))

    else:
      self.error(404)


class Sign(webapp2.RequestHandler):
  @xsrfutil.xsrf_protect

  def post(self):
    email = self.request.get('email')
    full_name = self.request.get('full_name')
    neighborhood = self.request.get('neighborhood') 

    if email == '' or not email.find('@') or full_name == '' or neighborhood == '':
      self.response.write('Invalid request. Please try again.')
      return;

    client = datastore.Client(config.PROJECT_ID)

    # Check if the email already exist
    query = client.query(kind='Signature')
    query.add_filter('email', '=', email)
    duplicate = list(query.fetch(1))

    # Update the old entry or create a new one
    if (len(duplicate) == 1):
      user = duplicate[0]
    else:
      key = client.key('Signature')
      user = datastore.Entity(key)

    # Pull a bunch of header data
    header_user_agent = self.request.headers['User-Agent'] if 'User-Agent' in self.request.headers else 'N/A'
    header_region = self.request.headers['X-AppEngine-Region'] if 'X-AppEngine-Region' in self.request.headers else 'N/A'
    header_city = self.request.headers['X-AppEngine-City'] if 'X-AppEngine-City' in self.request.headers else 'N/A'
    header_country = self.request.headers['X-AppEngine-Country'] if 'X-AppEngine-Country' in self.request.headers else 'N/A'

    user.update({
      'created': datetime.datetime.utcnow(),
      'email': unicode(email),
      'full_name': unicode(full_name),
      'neighborhood': unicode(neighborhood),
      'primary_district': unicode(get_primary_district(neighborhood)),
      'header_remote_address': unicode(self.request.remote_addr),
      'header_user_agent': unicode(header_user_agent),
      'header_region': unicode(header_region),
      'header_city': unicode(header_city),
      'header_country': unicode(header_country)
    })

    client.put(user)

    # Reset the count
    memcache.delete('count')

    # Add a cookie so the form is removed
    self.response.set_cookie('signed', 'true', max_age=63072000, path='/')
    self.redirect('/')


app = webapp2.WSGIApplication([
    ('/sign', Sign),
    ('/.*', MainPage),
], debug=False)
