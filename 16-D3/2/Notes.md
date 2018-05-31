## 16.2 - More D3: axes, data-binding, more bar charts, line charts

### Goals

* Build some actual charts using D3!
* Become more comfortable with binding data to elements.
* Import data from a CSV using D3.

### Why?

* Continue learning how to make custom visualizations using D3, build up data story-telling skills.

### Exercises

#### Exercise 0 - Demo HW (5 min)

#### Exercise 1 - D3 questions (Students Do) - (10 min + 10 min review)

* `merge(selection)` takes an existing selection as an argument. It merges together elements already on the page and new elements that need to be added to the DOM using `enter()`.
* See [this reference](http://d3indepth.com/enterexit/) for more on `enter()` and `merge()`.

#### Exercise 2 - Loading data from a CSV (10 min)

* First, simply opening the HTML page in your browser fails to work. We get a strange error loading the CSV file. See [this StackOverflow post](https://stackoverflow.com/questions/20041656/xmlhttprequest-cannot-load-file-cross-origin-requests-are-only-supported-for-ht) for more info.
* We have to run a local web server using `python -m http.server`, then hit `http://localhost:8000` in our browser. Our web server then "serves up" the CSV on the same host and port (localhost, 8000) as the HTML / JS, so we get no cross-origin error.
* `d3.csv()` works a lot like `d3.json()`: it takes as arguments 1.) the path to the CSV file you want to load, and 2.) a callback function that processes the data in the CSV.
* The data that gets passed to our callback function is an array of objects. Each property of our object is named according to the name of the header of each column.
* See [this reference](http://learnjsdata.com/read_data.html) for more examples of how to use `d3.csv()`.
* Using the `+` operator as a prefix, e.g. `data.hours = +data.hours`, *casts the value to the right of the operator to an integer*. This is equivalent to using `parseInt(data.hours)`. We have to cast `data.hours` because it's read as a string by `d3.csv()`.

#### Exercise 10 (from last class) - Building a Bar Chart (Instructor Do) - 10 min

* We see the standard SVG pattern: first, append an SVG element to the DOM, give it some width and height.
* Next, we see a new SVG element: `g`. The `g` element is a "group" of SVG elements. It functions conceptually like a `div`, allowing us to group arbitrary sets of elements together. We'll see why this is useful in just a moment.
* To create a bar chart, we see the data-binding pattern from Saturday's class: create "holes" for the rectangles we're about to fill in, bind our data to this selection, and run the `enter()` method to start a chain of methods that will run for all data not currently bound to elements (in this case, every piece of data).
* `rect` elements need 4 things: `x`, `y`, `width`, and `height`. To create a bar chart, each of these will need to be carefully selected.
* `width` is set manually. We'll see how to set this dynamically, based on the width of our whole chart, later.
* `height` is a function of the data: we just multiply the data tied to this bar by 10 (otherwise the bars would be tens of pixels small, which would be difficult to see).
* `x` is set to the current index of our elements (0, 1, etc.) * 60. Since the width of our bars is 50, this effectively gives us 10 pixels of spacing between each bar.
* `y` is the trickiest part of this: in order for our bars to be right-side up and flush against the bottom of the chart, we must subtract our height from some fixed value (here, the height of the SVG) to offset the `y` value as many pixel as we need. To see how this works, remove the `attr` method that sets `y` altogether and see how the chart renders without this.
* The `transform` attribute of the `g` element enables us to move everything within the `g` element (all the rectangles, in this case) a number of pixels from the left and from the top. This will become useful later when we need to add a bit of margin for our axes, axis labels, etc.

#### Exercise 3 - Building a Bar Chart from a CSV (Students Do) - 10 min + 5 min review

* Use the `README` for this one: there are a lot of hints to help you at each step of the way. There's also quite a bit of starter code.
* Creating a `g` (group) element allows all of the future elements in this "group" to be moved relative to the SVG. We translate (move) this element to the right and down according to the values in chartMargin

### **BREAK**

#### Exercise 4 - Scales (15 min)

* GOAL: facilitate the process of mapping values of our data -> pixel positions. e.g. when we create a bar chart, we need to know 1.) where to place the bars on the x axis, 2.) how high the bars need to be, 3.) the width of our bars, 4.) the height of our bars, and everything else we've been calculating manually. There must be a better way!
* It's not trivial to find the min and max values of an array in pure JS, but D3 comes with functions that help.
* `d3.min(arr)` returns the min value of an array
* `d3.max(arr)` returns the max value of an array
* `d3.extent(arr)` returns the min and max values of an array.
* `d3.scaleLinear()`, chained with its associated domain and range, returns a function (here we're calling that function `yScale`) that maps a value in the domain to its associated value in the range.
* `scaleLinear()` creates a function that associates a value in the domain with its proportional value in the range, given a linear scale (remember the equation for a line from math, `y = mx + b`).
* The `scaleBand()` method allows us to create a function that takes an array of categorical labels (usually strings, not numbers) and returns the associated position on the x-axis. It's typically used on the axis tied to the independent variable (here, that's the x axis).
* Given a scale function, we can run the `bandwidth()` method on that scale to find the width between each 
* [This reference](http://d3indepth.com/scales/) has more information on scales.

#### Exercise 5 - Axes (15 min)

* Since the coordinates of our SVG start at `(0, 0)` at the top left of the chart, we need to reverse the order of our range so that the scale is reversed (bottom to top, like normal charts appear) when we plot the chart.
* `.padding()` sets the spacing between the bands as a percentage of the band width. In this case, the padding is 5% of the band width.
* Next, create the `yAxis` and `xAxis` functions by using `axisLeft()` and `axisBottom()` respectively. D3's axis methods take a scale function as an argument and returns a function to the variable.
* Note that D3 has 4 available methods for this: `axisLeft()`, `axisRight()`, `axisBottom()` and `axisTop()`.
* [More notes on axes in D3](https://github.com/pshrmn/notes/blob/master/d3/axes.md)
* `call(func)` takes a function (`func` here) as an argument, calling the function on the selection (here we're applying the axis function to the selection, adding the axis to the group). `call` returns the original selection *so that we can keep chaining*.

#### Exercise 6 - Students Do Complete Bar Chart (15 min + 10 min review)

#### Exercise 7 - Instructor Do SVG paths (10 min)

* We can use SVG elements called paths to draw lines!
* The `path` SVG element takes a `d` attribute that specifies the path description.
* The `d` attribute takes commands. `M` takes an x, y coordinate as "arguments": where do we move the pencil to? `L` also takes an x, y coordinate, and tells the browser where to draw a line to.
* The `stroke`, `stroke-width`, and other properties of the path can be changed using CSS.
* `d3.line()` takes an array of coordinates (each element is an array of two elements) and generates a function that generates a path from an array.
* We pass the expression `lineGenerator(coordinates)` as the value of the `d` attribute, which appends the actual path to the SVG.
* We can use the scaling functions we've learned about to scale the values we pass to our line generator function.
* Moreover, we can set the `x` and `y` portions of our coordinates that `d3.line()` generates using the `x` and the `y` methods.

#### Exercise 8 - Students Do Generating Lines (10 min + 5 min review)

#### Exercise 9 - Instructor Do More Line Charts (10 min)

* `d3.timeParse()` takes a date format (here, `%Y`) as an argument, returning a function that will convert strings *in the given format* (i.e. a string like '2017') and convert that to a Date. So we'll pass in strings that look like years, and get back Date objects.
* We've seen a few functions like this now: given some parameters, return a _new function_ that will operate in a specific way.
* `xTimeScale` is our function to generate points on our x axis, and we're using `scaleTime()` to create a time-based scale. This works like linear scales, mapping a Date from the domain to a given point on the x axis (the range).
