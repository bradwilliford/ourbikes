# Our Bikes

A simple petition and bike share outreach site at https://ourbikes.org.

Public:

* [Homepage](https://ourbikes.org): Sign the petition
* [Supporters](https://ourbikes.org/supporters): Neighborhoods of supporters
* [Action Alert](https://ourbikes.org/actionalert?debug=true): Landing page for email campaigns

Admin:

* CSV Export of Data at /adminz


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
