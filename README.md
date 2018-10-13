# Our Bikes

A simple petition and bike share outreach site at https://ourbikes.org.

Public:

* [Homepage](https://ourbikes.org): Sign the petition
  * Set a cookie after the user submits so a 'thanks' message is displayed.
  * If a user moves, they can re-submit the form and we'll update their record by email.
* [Supporters](https://ourbikes.org/supporters): Neighborhoods of supporters
  * TODO: add new visualizations!
* [Action Alert](https://ourbikes.org/actionalert?debug=true&full_name=Jane%20Doe&neighborhood=San%20Francisco): Landing page for email campaigns
  * Generates a unique email for the supporter to send. With a random combination of input phrases and the user's name and neighborhood.

Admin:

* CSV Export of Data at /adminz. We use this to import supporters into [Mailchimp](http://www.mailchimp.com/monkey-rewards/?utm_source=freemium_newsletter&utm_medium=email&utm_campaign=monkey_rewards&aid=a1b97c965afa1a1543759ba94&afl=1).


## Development

### Setup

Install gcloud and App Engine for Python:

```
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
gcloud components install app-engine-python
gcloud auth application-default login
```

Install SASS:

```
sudo npm install -g sass
```

Install app requirements:

```
pip install -r requirements.txt -t lib
```

Set the Cloud project:

`our-bikes` is the id of the production Cloud project we use.

If your own staging demo or are making your own site, create a [new project](https://console.cloud.google.com/projectselector/appengine/create?lang=go&st=true&_ga=2.144302192.-414734393.1539453135) and update `PROJECT_ID` in `config.py`.

### Run locally

SASS:

```
sass --watch static/main.scss:static/main.css
```

App Engine:

Run:

```
dev_appserver.py .
```

And go to http://localhost:8080/.

### Deploy

```
gcloud app deploy app.yaml --project=our-bikes
```
