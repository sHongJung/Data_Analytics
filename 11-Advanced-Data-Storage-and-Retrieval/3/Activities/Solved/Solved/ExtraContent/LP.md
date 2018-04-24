### 05. Instructor Do: Introduction to Flask, API Design, &amp; the Web (0:15)

* Explain that, today, we'll lay a foundation by studying the most fundamental elements of the web, namely:

  * Client-server architecture

  * Endpoints and the request-response cycle

* Take a moment to articulate and demonstrate a typical interaction with the browser:

  * First, we type in a URL

  * Then, we wait...

  * ...And, eventually, something pops up on the page (whether it be the site we asked for, or an error message of some sort)

* Point out that, in this interaction, we _ask_ for something&mdash;the content of the website&mdash;and eventually, get what we asked for (or an error).

* Point out that, conceptually, there are two major entities involved in this interaction: The **client** and the **server**.

* First, there is the **client**. That's us&mdash;whoever _asks_ for information is the client.

  * Emphasize that a client is just a person (or, more precisely, a program) that makes a request for something.

* Then, there is the **server**. Whoever sends us the information we ask for is the server.

  * Explain that a server is just a program that fulfills someone else's request for something.

* Emphasize the previous point before moving on:

  * A **client** is an entity that asks for something.

  * A **server** is an entity that hears a client ask for something, and then provides it.

* Explain that, in order for servers to be able to give clients what they ask for, they need clients to provide some special pieces of information.

  * Clients must specify _what_ information they want; _where_ the server should send it (client IP address); etc.

* Explain that the client sends all of this information in an object called a **request**.

  * Reiterate that a request contains information about what a client wants the server to provide, as well as any metadata the server needs to fulfill the request.

* Explain that these requests "objects" must adhere to a very specific format.

  * For example, a request for a website's home page might look like this: `GET /index.html HTTP/1.1`.

  * Explain that this tells the server to "get" the file `index.html`, and send it back to the client.

* Point out that this request is just a string written in a special format.

  * Emphasize that the details of this request are not important at the moment.

  * Rather, the takeaway point is that this request adheres to a **specific format**.

* Explain that, once the server receives this specially formatted request, it will run code to figure out how to find what the client asked for.

  * Once it finds what the client requested&mdash;in the case of the above example, the `index.html` page&mdash;it sends back its _own_ specially formatted **response**.

  * Explain that a given client request triggers the server to send **exactly one response**&mdash;in other words, any given request triggers the server to send _at most one_ response.

* Explain that, like requests, servers must send responses in a specified format that clients expect.

* Explain that such "specific formats", which define standard ways for programs to talk to one another, are called **protocols**.

  * Reiterate and emphasize the informal definition of "protocol": "A protocol is a set of rules that make it easy for programs to share data with one another."

  * Explain that the proper format for a request is defined by the **HTTP protocol**.

* Reassure students that the _details_ of the HTTP protocol, etc., are (fortunately!) abstracted away from us by libraries like requests.

  * However, emphasize that students must at least be aware of the client-server model and the request-response cycle.

* Slack out this [diagram of client-server interaction](https://cdn.techterms.com/img/lg/client-server_model_1253.png).

  * Point out that a computer, smartphone, etc., can all qualify as a client. Emphasize that the nature of the device is irrelevant&mdash;what characterizes a client is simply that it is the entity **making the request**.

  * Explain that this model describes the basic architecture of the Internet.

  * Explain that essentially all "normal" interactions we have on the web involve a client requesting something from a server.

* As an analogy for the client-server model, explain that, in a restaurant, a customer placing an order acts as a _client_, who makes a request for a dish; and the kitchen and wait staff act as the _server_, who fulfill the request.

* Point out that, when we visit a website&mdash;such as the [Weather Channel](http://weather.com)&mdash;we're typically greeted with a web "page", with textual content, images, etc.

  * Explain that this is, of course, standard for sites meant to be consumed by _humans_.

* However, remind students, when we make requests of APIs, we do _not_ get back responses with images, formatted text, etc.

* Remind students that, when working with APIs, we typically receive raw data.

* Point out that, as data analysts, we're more interested in such sources of immediately consumable data rather than "human-facing" websites.

* Remind students that _client_ is simply an entity that makes a request.

  * Point out that this makes any scripts we write with `requests` _clients_ of the API(s) they use.

  * So, this means students have already been writing client code for weeks!

* Explain that today's lesson will introduce students to the tools required to build the _other_ side of this interaction.

* Finally, point out that, when we browse a website, we typically visit a series of _different pages_.

  * Similarly, point out that, when we use APIs, were typically able to get back many different kinds of data, depending on what we ask for.

  * Point out that this means clients can make a series of _different requests_, each of which triggers a _different response_.

* To demonstrate, open the below sites in the browser, and simply point out that the data differs between the pages.

  * [Posts Endpoint](https://jsonplaceholder.typicode.com/posts)

  * [Users Endpoint](https://jsonplaceholder.typicode.com/users)

* Emphasize that the data for each link is unique.

  * Point out that simply changing the final word of the URL from `posts` to `users` completely changed the data we received.

* Explain that this occurs because the server uses the URL of a request to determine how to respond.

  * Explain that the URLs that trigger unique responses are called **endpoints**.

* Explain that, as API developers, we are responsible for configuring how a server responds to requests to given endpoints.

* Explain that, today, we will be using a library called [Flask](http://flask.pocoo.org/) to **create servers** and **associate different responses with different endpoints**.

* Take a moment to address any student questions before moving on.


### 18. Students Do: Chinook Database Analysis - Part 2 (0:20)

* Slack out the solution for [Activities/Solved/08-Stu_Chinook_Part1/Stu_Chinook_Part1.ipynb](Activities/Solved/08-Stu_Chinook_Part1/Stu_Chinook_Part1.ipynb). Students can use the queries from this solution to complete part 2 of the activity.

* Ask the students to switch their focus to completing the Flask api for their queries.

* Explain to the students that they can use their queries or the solution provided.

### 19. Everyone Do: Review Chinook Database Analysis Part 2 (0:10)

* Open [Activities/Solved/09-Stu_Chinook_Part2/app.py](Activities/Solved/09-Stu_Chinook_Part2/app.py) and walk through the solution.

* Explain that for this application, we will use the code from part 1 with flask and jsonfify to serve our query results as JSON objects.

* Show students that we establish our database ORM connections and initialize our Flask app.

* The root route `/` for this application is simply documentation for our available routes.

* Explain that route `/api/v1.0/countries` simply converts the query results into a list of countries using `list` and `np.ravel`. List comprehensions or for loops could also be used to extract the countries from the query results and place them into a list. We use jsonify to return the list as a JSON response object.

* For the next route, `/api/v1.0/countries/invoice/totals`, we need to extract two values for each result in the list of query results. We choose to do this with a by first converting to a list of Python Dictionaries.

* Explain that one approach to having default url parameter values in Flask is to assign multiple route decorators with a default value for the url parameter. In the case of `/api/v1.0/postalcodes/<country>`, when no country is specified in the url, the default value of 'USA' is used in the query.

* Similarly, the route `/api/v1.0/invoice/total/<country>` uses a default value for country. In this response, we must also convert the sqlite column type of `Decimal` to a Python `float` in order for jsonify to translate the value into valid JSON.

* In our final route, `/api/v1.0/postalcodes/totals/<country>`, we again have a default value of 'USA' for the country. This query also requires unpacking multiple values from the list of tuples that the query returns. We choose to use a Python dictionary to hold the results values for Billing Postal Code and the Invoice Items Totals. We append each dictionary to a list and return the list of dictionary objects and JSON using jsonify.


