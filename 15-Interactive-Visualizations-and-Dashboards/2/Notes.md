## 15.2 - Advanced Charts with Plotly

[Small PPT to begin class](https://docs.google.com/presentation/d/1jsxQ03FlzpHd5SVGN6N2Ix_R3DBXHeLMYJSDQ_9j1jY/edit?usp=sharing)

### Goals

* Cover more chart types in Plotly.
* Manipulate charts using JS events (e.g. from dropdown choices, button clicks, etc.)
* Most importantly, this is meant as a review day. If we need to go slower, we can.

### Why?

* Plotly gives us so much for free when we want to create charts, and provides a lot of customization options.
* Develop more visualizations so y'all get comfortable using Plotly's Javascript API.
* Introduce you to more advanced plots (e.g. candlestick charts) so you're aware of them and so you can think about how to apply them in the real-world.
* Varying chart data by selecting choices in drop-down menus (one of the things we'll cover today) is on the HW for this week's content.

### Notes

* Today, I'll spend time showing off the key features of charts and how they work _before_ you do the exercise, so it's clear what you're building, why it's important and how it works.
* Sometimes I make edits to notes or other examples right before class, so please always `git pull` as we start class.

### Exercises

#### 0 - Plotly.js refresher

* Always include link to Plotly JS in `<head>` tag.
* Make sure you have somewhere to draw your chart (typically we just create an empty `div` element in our HTML, so we can render the chart there later).
* Charts are created using two core JS objects: 1.) an array of traces, which contain our data and information about the plot type, and 2.) the layout object that specifies formatting options for our chart.
* The properties of our data and layout objects correspond to specific pieces of the chart (e.g `title` corresponds to the title). These properties are all enumerated in the [Plotly.js reference](https://plot.ly/javascript/reference/).
* [This Observable notebook](https://beta.observablehq.com/@jashkenas/plotly-js) has some great Plotly examples you can edit inline. Observable notebooks are new but attempting to become the Jupyter notebooks for JavaScript.

#### 1 - Dropdown events, `switch` statements, and `Plotly.restyle` (10 min)

* Here, we control the data we show on our chart by changing the value of the dropdown menu below the chart.
* The `select` creates a dropdown menu, with the options specified by the included `option` elements.
* We include an [`onchange` attribute](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onchange) in our `select` element. This attaches an event listener to this element for the [change event](https://developer.mozilla.org/en-US/docs/Web/Events/change), which fires when the user changes the value of the dropdown.
* Conceptually, this is the same as selecting elements and using `addEventListener` to run a callback function on a given event, like we'd seen before. This can simplify the code necessary to add event listeners, and it can be easier to tell that there's an event listener to begin with (you can immediately tell by looking at the HTML).
* `getPlot` is a function we define in `plots.js`, so we load `plots.js` before our `select` element is loaded to ensure the code is available when we load the element.
* `this.value` represents the new value of the element after the value is changed!
* The `init` function sets the initial data in our plot.
* The `switch` statement evaluates an expression and runs the code included in the `case` statement corresponding to the value of the expression.
* *Remember to include a `break` statement at the end of each `case`*. See the Examples section of [this MDN reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch).
* The code within the `default` section runs if none of our cases above match the target value. This can be helpful here if you add another option to your `select` element but forget to update this code. There, you'll still handle the change, since the `default` case will run.
* [`Plotly.restyle`](https://plot.ly/javascript/plotlyjs-function-reference/#plotlyrestyle) takes a number of different arguments in different cases (see the docs for examples). Here, we're passing 1.) the ID of the element containing the plot we want to change, 2.) the attribute of the data object we want to change and 3.) the value of the data. Here, `restyle` requires brackets around our `x` and `y` data. There are a few different ways to do this (e.g. creating a whole new plot).

#### 2 - Students Do Dropdown Events (10 min)

#### 3 - Students Do Time Series data (15 min)

* *Let's sign up for a Quandl API key first*.
* Now let's take a look at what we're building towards in this example.
* `Plotly.d3.json` fetches JSON just like the `d3.json` method we saw last week. In fact, it's the same method - Plotly is based on D3 and we can access D3 method using the `Plotly.d3` object.

#### 4 - Students Do Dynamic Time Series Data (15 min)

* This time, users get to select the stock you want to plot!
* Attach an event listener on the submit button.
* Use the user's selected stock to retrieve the associated data from Quandl.
* Plot the data returned from Quandl as we did last exercise.
* You must use `Plotly.d3.select('#stockInput').node().value` to get retrieve the first DOM element with the id `#stockInput`, and get its value using the `.value` attribute.
* [Reference on preventDefault()](https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault)

#### 5 - Students Do Candlestick plots

* A good visualization densely communicates information simply.
* [Candlestick charts](https://en.wikipedia.org/wiki/Candlestick_chart) are one example of a dense visualization.
* The candle is red when the closing price is lower than the opening.
* The candle is green when the closing price is higher then the opening.
* Any "wicks" outside the candle (the vertical lines extending from either end) are the high and low price for the day (some may be difficult to see, or not present at all).
* This visualization contains a large amount of data. A trader can look at this and understand whether the daily change was positive, what the rough magnitude of that change was, whether there was high intra-day volatility for this particular stock (big highs and lows), etc.
* We need to pass `x`, `high`, `low`, `open`, `close` properties to the trace object we use to draw our plot. The `type` must be `candlestick`.

#### 6 - Intructor Do Rolling Averages

* The movement of stock prices is "jagged". You can see the overall trend across a long period of time but small sections have a lot of noise.
* To visualize the general trend, it make sense to use a rolling average. This "smooths" the day-to-day rises and dips and reduces the noise of the chart.
* In this case, we're taking a rolling average of the last 30 days, inclusive of the current date.

#### 7 - Students Do Stocks Report

* For the bonus, I'd typically use a library like [Moment.js](https://momentjs.com/). The code would simplify to `moment().format("MMM YY");`
