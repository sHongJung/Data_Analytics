### Goals

* Today we'll build an app that uses Flask, SQLAlchemy and Plotly together.
* Previously we've only rendered basic HTML / JSON from databases. Now we're finally visualizing data from our database using Plotly.
* We've seen that SQLAlchemy is a powerful way to query SQL DBs. Flask helps us run these queries in response to HTTP requests. Finally, we've used `d3.json` to fetch data from our API (in this case, we're using Flask as our API).
* There are fewer new concepts tonight than normal - we're mainly integrating what we've already learned together.

### Why?

* On the job, you'll be storing data in SQL databases that you want to visualize using JavaScript. This requires we query an via HTTP using JavaScript, and query our database from that API.
* Tonight is one of those classes where we tie things together. I hope you feel powerful building these applications!

### Notes

* JavaScript can be very confusing the first time through. Y'all should be very proud of yourselves for getting this far, even if it doesn't all make sense yet. You have made incredible progress.
* While I'm still learning names, it would help if you upload a picture of yourself in BCS so I can easily match faces to names!
* Just a friendly reminder: please post topics you want to see covered during JavaScript office hours in Slack.

### Exercises


#### 1 - Instructor Do Basic Flask + Plotly (15 min)

* GOAL: develop our first Flask app that renders a Plotly chart.
* Our homepage (The "/" route) returns our `index.html` file.
* Remember that, since Plotly is built using `d3`, we can access the `d3` object using `Plotly.d3`.
* Here, that means we can run `Plotly.d3.json` to fetch JSON from an API.
* Remember that `d3.json` fetches JSON from some URL (the first argument we pass to `d3.json`). 
* NOTE: we simply pass `/line` as the URL here. As with other cases we've seen, passing a relative resource name (`/line` vs. `http://127.0.0.1:5000/line`) makes a request to that resource *on the current hostname* (the website you're currently viewing).
* Naturally, we want to do something with that response. So we can pass a second argument to `d3.json`: the callback function that we run whenever the response is returned, or when there is an error in the request.
* In this particular case, we've made it very easy to plot data with Plotly, since our `/line` route returns data in the exact format we need to pass to the `Plotly.plot` call.
* `Plotly.plot` is just like `Plotly.newPlot` (accepts all the same arguments). We just can't call `Plotly.plot` mutliple times in a row, like we did in Lesson 15.1. Here, that's OK - we only need to call it once.
* Recall that the `jsonify` function from the `flask` Python module takes a Python data structure (a list, a dictionary, etc.) and returns the JSON string equivalent (JSON technically gets returned to the browser as a string).
* PARNTERS DO: walk through the step by step flow for what happens when you hit the "/" route. Use the most technical language you can.

#### 2 - Students Do Lyric Frequency (15 min + 10 min review)

* I know I said you'd never see another pie chart in this class again... so I want you to critique this one.
* Key takeaway: if you're just going to plot your data using Plotly, format your Python list / dictionary to return a format Plotly understands, so you don't have to do as much work in JavaScript formatting the API response.
* There are a number of ways we can extract the data from our `lyrics` `Counter` object. Two ways are included in `app.py`. For #2, using `zip`, see [this reference](https://stackoverflow.com/questions/12974474/how-to-unzip-a-list-of-tuples-into-individual-lists).

#### 3 - Instructor Do Emoji Charts (15 min)

* [Why are we using the flask\_sqlalchemy package, vs. just SQLAlchemy](https://stackoverflow.com/questions/14343740/flask-sqlalchemy-or-sqlalchemy)?
* We're now connecting our Flask app to a SQLite database so that we can run queries on the data in that DB and visualize the results of those queries.
* We have three separate routes, each of which visualizes a similar dataset.
* Our `select` element has three options: one for each of our datasets. *The `value` attribute tied to each `option` is the same as the name of the route.*
* The `onchange` attribute on the `select` element lets us run a function when the value of the dropdown menu changes.
* In this case, we run a `getData` function, which accepts as an argument `this.value`, the current value the user selected.
* Since the value we're passing to `getData` is the name of a Flask route, in this particular case, we call the argument `route` when we define the `getData` function.
* ```/${route}``` uses "template literal" syntax, which is just a fancy way to format strings, replacing parts of the strings with variables. This formatted string gets replaced with the name of the route the user chooses from the dropdown menu (e.g. `/emoji_char`).
* Just like the exercises before, we're formatting a Python object we can return to the browser in the format Plotly expects.
* PARTNERS DO: walk through this code at a *high level* with each other, explaining to one another how the process works step by step (from the initial request to `/`, when we change the options in the drop-down menu, etc.)

#### 4 - Students Do Bigfoot Sightings (20 min + 10 min review)

* This example uses the `sqlalchemy` module to connect to the DB and reflect existing tables. The code is provided for you.
* `jinja` template syntax allows us to load JavaScript external to our HTML, using the `url_for` function. e.g. `<script src="{{ url_for('static', filename='js/app.js') }}"></script>` loads a file from `static/js/app.js`.
* The `results` object we get back from SQLAlchemy is a list of tuples. Each tuple contains (year, number of sightings for that year).
* We can extract just the years, or just the sightings, using list comprehension syntax, e.g. `years = [el[0] for el in results]`

#### 6 - Instructor Do - More requests with Flask (20 min)

* Key takeaway: we can accept user-submitted data (often from forms) with a `POST` request in Flask.
* So far, we've just created routes in Flask that accept `GET` requests (your browser makes a request to _fetch_ data).
* Now, we can configure a Flask route to accept `POST` requests using the `methods` argument on the call to `@app.route`.
* [A small reference on GET vs. POST](https://www.w3schools.com/tags/ref_httpmethods.asp)
* The `methods` argument takes a list of strings corresponding to the HTTP methods this route will accept.
* For example: `@app.route("/send", methods=["GET", "POST"])`
* Then, within the function tied to the route, we need to handle `POST` requests accordingly. If our route accepts _both_ `GET` and `POST` requests, we need to have a conditional statement tha checks for the method type. Flask gives us the method type in the variable `request.method` (this will be "POST" for `POST` requests, "GET" for `GET` requests, etc.)
* For POST requests, we can access the data the user submitted via the `request.form` variable, which is a dictionary containing values tied to the input fields we submitted. The keys of this dictionary correspond to the 'name' attributes of the input fields in the form.

#### 7 - Instructor Do - Saving POST data to a DB with SQLAlchemy (15 min)

* So far, we have gone over retrieving and submitting information with GET and POST routes. But the data is not permanently saved, and is lost when we quit the server app.
* Key takeaway: the core difference between this and the last exercise is that we're using the SQLAlchemy methods we learned before to add new records to the SQLite DB.
* We load the `/send` endpoint and submit the form to add a new pet to the DB.
* After retrieving the form data from the `request.form` dictionary, adding data to the DB is a 3 step process: 1.) create a new `pet` object of class `Pet`, passing in the `nickname` and `age` as arguments. 2.) Run `db.session.add(pet)` to add a new record to our SQLAlchemy session. 3.) Finally, run `db.session.commit()` to write any changes we've added to our session to the database. This last step is required to persist the data to our SQLite DB!
* The code that starts with `@app.before_first_request` (the `setup()` method) drops all existing records from the DB and re-creates the schema from scratch on each restart of the Flask app.
* Remove the `setup()` method with the associated `@app.before_first_request` decorator. Start the Flask server and add some pets. Quit and restart the server. The `/pets` endpoint should still list the pet you'd added *before you restarted the server*.

#### 7 - Students Do - Pet Pals (25 min + 10 min review)
