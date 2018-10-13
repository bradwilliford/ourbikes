from google.cloud import datastore
import config
import datetime
import google.appengine.api.users as users
import jinja2
import logging
import main
import os
import webapp2


class MainPage(webapp2.RequestHandler):
  def get(self):
    if not users.is_current_user_admin():
      return

    client = datastore.Client(config.PROJECT_ID)
    query = client.query(kind='Signature')
    signatures = list(query.fetch())
    count = len(signatures)

    known_emails = []

    for signature in signatures:

      if signature['email'] in known_emails:
        logging.info(signature['email'])

      known_emails.append(signature['email'])

      name_split = signature['full_name'].split(' ')

      # Handle initials like "A J Parker"
      if (len(name_split[0]) == 1 and len(name_split[1]) == 1):
        signature['first_name'] = name_split.pop(0) + ' ' + name_split.pop(0)
      else:
        signature['first_name'] = name_split.pop(0)

      signature['last_name'] = ' '.join(name_split)

    template_values = {
      'signatures': signatures,
      'count': count
    }

    template = config.JINJA_ENVIRONMENT.get_template('templates/admin.html')
    self.response.write(template.render(template_values))


def chunks(l, n):
  chunks = []
  # For item i in a range that is a length of l,
  for i in range(0, len(l), n):
    # Create an index range for l of n items:
    chunks.append(l[i:i+n])
  return chunks


class UpdateEntries(webapp2.RequestHandler):
  def get(self):
    if not users.is_current_user_admin():
      return

    # client = datastore.Client(config.PROJECT_ID)
    # query = client.query(kind='Signature')
    # signatures = list(query.fetch())

    # chunk_lists = chunks(signatures, 500)
    # for chunk in chunk_lists:
    #   for signature in chunk:
    #     signature.update({
    #         'primary_district': unicode(main.get_primary_district(signature['neighborhood']))
    #       })
    #   client.put_multi(chunk)

    # self.response.write('Done.')


app = webapp2.WSGIApplication([
    ('/adminz', MainPage),
    ('/adminz/update', UpdateEntries),
], debug=False)
