### INSTALL HEROKU

https://devcenter.heroku.com/articles/heroku-cli#download-and-install

Do you have an older version installed? Type `which heroku` to find and delete it.

### GET CODE

cd to your code directory

https://github.com/mattalytics/heroku_demo

 `git clone git@github.com:mattalytics/heroku_demo.git`

`cd heroku_demo`

`heroku login`

`heroku create`

`heroku config:set consumer_key=`
`heroku config:set consumer_secret=`
`heroku config:set access_token=`
`heroku config:set access_token_secret=`

### Make some edits to file to print out a few lines

`git push heroku master`

`heroku ps:scale worker=1`

`heroku logs`

it worked!

OPTIONAL - Create an API Server

`conda create -n herokuapi python=3.4`

`pip install gunicorn flask tweepy`

add `app.py`

add line to procfile: `web: gunicorn app:app --log-file=-`

`pip freeze > requirements.txt`

commit your changes and push

`heroku ps:scale web=1`

voila, an extremely basic api accessible to all

