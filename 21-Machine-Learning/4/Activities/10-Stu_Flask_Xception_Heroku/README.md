### Xception Flask Deployment

* Follow the instructions below to deploy the Xception powered machine learning app to Heroku.

## Instructions

* Make sure you have an `Uploads` folder to hold your uploaded images.

* Add the `Procfile` and `requirements.txt` file.

* Add the `gunicorn` web server to the `Procfile`.


```
web: gunicorn app:app
```

* Add the following package requirements to the `requirements.txt` file.


```
certifi==2017.7.27.1
click==6.7
Flask==0.12.2
gunicorn==19.7.1
itsdangerous==0.24
Jinja2==2.9.6
MarkupSafe==1.0
Werkzeug==0.12.2
Pillow==4.2.1
numpy==1.13.1
h5py==2.7.0
tensorflow==1.1.0
Keras==2.0.6
```

* Test the app locally to make sure that it runs.

* Finally, follow the Heroku deployment guide to create and deploy the app.


```
git init
git add .
git commit -m "init repo"
heroku create
git push heroku master
heroku open
```

## Hints

* Use the [Heroku Deployment Guide - Deploying with Git](https://devcenter.heroku.com/articles/git) for reference.
