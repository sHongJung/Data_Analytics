## 16.3 - Line Charts, Scatter Plots, and more D3

### Goals

* Review line charts from last time
* Plot multiple datasets on the same chart + multiple axes
* Use event listeners on D3 charts.
* Develop a scatter plot.
* Create tooltips, transitions

### Notes

* Thank you for the feedback this week. One key takeaway: people seem to like the focus on the concepts, but we need to make sure we cover all the exercises. I'll aim to keep the conceptual overview but move a bit quicker today. I know the pace with D3 has been fast, but I want to make sure y'all get a good conceptual overview of the exercises, even if all the code doesn't make sense at first.
* With that said, we are likely to skip a couple of exercises because I don't think they add much to this lesson.
* I want to re-iterate that it's OK to be confused about this material the first time through. D3 is a complex (and powerful!) library. The only way to truly learn this is to write a lot of D3 code.
* Remember that you'll want to run `python -m http.server` in the appropriate directory before running these examples so that you serve all local files (e.g. CSVs) using a web server.

### Exercises

#### Exercise 1 - Instructor Do Line Charts (15 min)

* We're pulling data from a CSV using `d3.csv()` here.
* `d3.timeParse()` takes a date format (here, `%d-%b`) as an argument, returning a function that will convert strings *in the given format* (i.e. a string like '30-Apr') and convert that to a Date. So we'll pass in strings that look like years, and get back Date objects.
* Check out [this reference](https://github.com/d3/d3-time-format#locale_format) for a list of the date format "specifiers" you can use here.
* `d3.line()` takes an array of coordinates (each element is an array of two elements) and generates a function that generates a path from an array.
* We pass the expression `lineGenerator(coordinates)` as the value of the `d` attribute, which appends the actual path to the SVG.
* We can use the scaling functions we've learned about to scale the values we pass to our line generator function.
* Moreover, we can set the `x` and `y` portions of our coordinates that `d3.line()` generates using the `x` and the `y` methods.
* We've seen a few functions like this now: given some parameters, return a _new function_ that will operate in a specific way.
* Remember that preceding a value with a `+` sign casts it to an integer (the data from our CSV is read in as strings).
* [`d3.scaleTime()`](https://github.com/d3/d3-scale#scaleTime) is a scale function similar to the ones we've seen before. In this case, we're scaling Date values in the domain to coordinate values in the range.
* Key takeaway: all the scale functions we've seen map some type of data (numbers, categorical data on the x-axis, and now dates) to pixel coordinates on the screen.
* [`d3.max`](https://github.com/d3/d3-array#max) can take an optional function as the second argument, called an "accessor" function, which allows us to retrieve a specific value from elements of an array. Since we have an array of objects here, we need to extract specific values from each object (each element).
* The "ternary" operator has a funny name, but it simplifies the syntax for a common operation: returning one value if a condition is true, or returning a different value if a condition is false.
* The syntax reads: `condition ? return this value if condition is true : else return this value`.
* The comments in `app.js` contain the equivalent if / else statement so you can see how this compares.
* [`d3.line`](https://github.com/d3/d3-shape#lines) constructs a new "line generator", which is a function that generates a path description tied to the data for the line we want to draw.
* Below, we'll call this line generator *for each of the elements in the array of data tied to our `path` element*. It will take the element, run the function, and create the path description that joins each of the (x, y) coordinates together.
* We set the `x` data of the line here to be the x coordinates corresponding to the date (remember: `xTimeScale` is a function that takes a date and returns the x coordinate where we should place that date on the canvas).
* We set the `y` data of the line to the y coordinates where `yLinearScale` says we should place the y coordinates, given the domain and range defined before.
* To create the line, we must only create a new `path` element and then set the `d` attribute to be the path description returned by running `line1` or `line2` on our data array.

#### Exercise 2 - Everyone Do Line Chart with Multiple Axes (15 min)

* Key takeaway: when the y scale of your data are vastly different, it'll be difficult to see the trend in the data with the smaller scale. In this case, it might make sense to use multiple axes.
* [This reference](https://datahero.com/blog/2015/04/23/the-dos-and-donts-of-dual-axis-charts/) notes some "do's and don'ts" with multiple axes.
* What's required to create multiple axes? 1.) Two distinct scaling functions for our y-data: one for the morning data, and another for the evening data. 2.) creating two axes, each using the corresponding scale functions.
* When creating our second axis, we have to apply a transformation (translating the right-axis by `width` pixels to the right)

#### Exercise 3 - Adding Legend, Coloring our Axes (10 min)

* Setting the `stroke` attribute allows us to change the color of the axis labels
* We can add legends by adding a `text` SVG element to our chart. We apply a transformation to get the text in the right place, and then set a handful of attributes that centers the text (`text-anchor` anchors the text around a point), sets the fill, and adds the actual text we want to display using the `text()` method.

#### Exercise 4 - Students Do Adding Multi-line chart with Multiple Axes (15 min + 5 min review)

#### Exercise 5 - Instructor Do Responsive Charts, Event Listeners with D3 (10 min)

* The [window object](https://www.w3schools.com/jsref/obj_window.asp) represents a window containing a DOM document in the browser. `window` has some special events (like resize) and properties (like `innerWidth`) that we'll use here.
* The first event listener we create is a listener on this `window` object. The `resize` event doesn't get fired on specific elements. It's the window itself (represented by `window`) that actually gets resized.
* Each time the window is resized, we run the `makeResponsive` function, removing the SVG and creating it again completely anew. Each time, we set the width and height of the SVG (along with the width, height and position of the chart elements inside it) based on the value of `window.innerWidth` and `window.innerHeight`, which represent the size of the user's browser window in pixels.
* We use our data-binding pattern to create rectangles for each piece of data. On these rectangles, we add two event listeners: one on click and another on mouseover.
* On each `click` event, we fire an alert in the browser (but you can run any JavaScript code you want within this function).
* On each `mouseover` event, we set the fill of the rectangle to be red.
* Typically, `mouseover` events must be paired with an associated `mouseout` event. In this case, we change the color of the rectangle back to green.

#### Exercise 6 - Instructor Do Tooltips (10 min)

* The `toolTip` variable creates a new `div` to the body of the page, which is **hidden by default**.
* Since our tooltip is a div, we can set the HTML that we want displayed within our tooltip using the `html()` method, on mouseover. This function says: change the "display" to "block" (first, unhide the div), set the HTML to the pizzas eaten for the current circle we're mousing over, and position the `div` where our cursor currently is (`d3.event.pageX` and `d3.event.pageY` gives us the location on the page where the current event (the mouseover) happened, i.e. the place where we moused over the circle.
* On our `mouseout` event listener, we hide the div again by setting the display style to "none".

#### Exercise 7 - Students do Tooltips (10 min + 5 min review)

#### Exercise 8 - Tooltips with d3-tip (10 min)

* Here, we're using [d3-tip](https://github.com/Caged/d3-tip), a third-party library that helps us create tooltips.
* We create a tooltip using `d3.tip()`, and chain other methods from there. We need to attach a class, offset the tooltip (offset from the [top, left](https://github.com/Caged/d3-tip/blob/master/docs/positioning-tooltips.md#tipoffset)), and set the HTML of what the user sees inside of the tooltip.
* Like with axes, the `.call()` method actually runs the code that generates the tooltip, attaching it to the chartGroup to which we attach all of our chart elements.
* `toolTip.show(d)` shows the tooltip, accepting the current piece of data as an argument. Remember above, the `html()` method also accepted a function, which took the piece of data passed to it and displayed the relevant HTML accordingly. Here we're just passing the data down so that function can use it.

#### Exercise 9 - Students Do Hair Metal Bands (20 min + 10 min review)

#### Exercise 10 - Instructor Do Transitions (10 min)

* Key takeaway: transitions enable you to move from one state to another over some period of time. Here, we're just going to change a rectangle from green to red. In the abstract, this concept will be incredibly powerful for adding animations that draw users in to your data story.
* The `transition()` method starts a transition. It says: I'm about to transition from the state (color, size, etc.) that this element was before, and I need you to specify the state I'm transitioning towards now.
* We chain a `duration()` method to our transition object, which specifies how long the transition from state A -> B should last, in milliseconds.
* Finally, we tell D3 what our final state should be: in this case, we're just changing the fill of the rectangle to red.
* On mouseout, like we've been doing, we just reset our state.

#### Exercise 11 - Students Do Transitions (10 min + 5 min review)

#### Exercise 12 - Partners Do Review Hair Metal Code (15 min + 10 min review)
