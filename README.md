# Our Bikes

A simple petition and neighborhood outreach site for bike share at ourbikes.org.

## Setup

Install gcloud and App Engine for Python:

```
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
gcloud components install app-engine-python
```

Install SASS:

```
sudo npm install -g sass
```

Install app requirements:

```
pip install -r requirements.txt -t lib
```

## Dev

SCSS:

```
scss --watch static/main.scss:static/main.css
```

App Engine:

```
dev_appserver.py .
```

## Deploy

```
gcloud app deploy app.yaml --project=our-bikes
```
