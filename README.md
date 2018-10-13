# Our Bikes

A simple petition and bike share outreach site at https://ourbikes.org.

Public:

* [Homepage](http://ourbikes.org): Sign the petition
* [Supporters](https://ourbikes.org/supporters): See neighborhoods of supporters
* [Action Alert](http://ourbikes.org/actionalert): Landing page for email campaigns

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
```

Install SASS:

```
sudo npm install -g sass
```

Install app requirements:

```
pip install -r requirements.txt -t lib
```

### Run locally

SCSS:

```
scss --watch static/main.scss:static/main.css
```

App Engine:

```
dev_appserver.py .
```

### Deploy

```
gcloud app deploy app.yaml --project=our-bikes
```
