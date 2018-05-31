# 16.1 - More D3

### Goals

* Learn how to bind data to elements (we'll learn what that means!)
* Learn how to use SVG (Scalable Vector Graphics)
* Bind SVG elements to data
* Create a basic bar chart using D3

### Why?

* When you want full control over a powerful visualization, D3 is the go-to library.
* D3 supports many more complex chart types than Plotly.
* You can build [Tetris](http://d3tetris.herokuapp.com/), charts that [transition over time](https://bost.ocks.org/mike/nations/), or charts that [map more complex data, like wind, to visualizations](http://charts.animateddata.co.uk/ukwind/). There are many more examples in the [D3 Gallery](https://github.com/d3/d3/wiki/Gallery).
* When you want to develop quick charts without a huge amount of customization, choose Plotly. When you need more control, use D3.
* We'll start out learning how to draw basic shapes, which we'll then use to make our own charts.

### Notes

* **Please `git pull` the student repo**
* Some of these concepts can be quite difficult to get the first time. I would re-do these exercises from scratch and review the associated resources in that section of the notes. It'll be a great review of both JavaScript and D3.
* Review session after class on some JavaScript fundamentals.
* [A little bit about me](https://docs.google.com/presentation/d/1jsxQ03FlzpHd5SVGN6N2Ix_R3DBXHeLMYJSDQ_9j1jY/edit#slide=id.p)

### Exercises

#### Exercise 0 - Learn something new about D3 (10 min)

* Read over the [D3 Homepage](https://d3js.org/) and review the [Gallery](https://github.com/d3/d3/wiki/Gallery).
* I'll call on random people to tell us something new about D3 that we didn't learn last week.
* Q: what does D3 stand for? What does that mean?
* Q: what types of charts can you create using D3?
* Q: what is data binding?
* D3 has many methods to work with data. We've covered some, and we'll cover more this week.
* Selections make it easy to create, read, and update elements in the DOM.
* "Method chaining" makes it easy to run methods on selections (e.g. `d3.select('#id').text('new text here')`).
* Transitions let us apply changes to elements over time, e.g. changing the background of a page from white to black slowly, not immediately. We can change the size of a circle from small to large.

#### Exercise 1 - Everyone Do Data Binding (25 min)

* Data binding refers to the process of attaching data to elements of the DOM. The whole point of what we're going to learn today is how to visualize _data_ using D3. So we need a way to associate the data we want to visualize with the elements that will present that data on the screen.
* The goal of this exercise is to understand how data binding works in D3. We'll be working with `li` elements, since it's easy to see how data binding works here. But we'll quickly move on to creating more complex shapes (rectangles, circles, etc.).
* The `index.html` file in this exercise has a `ul` element with three `li` elements within it.
* Q: how would you select each of the `li` elements within the `ul`?
* The [`each`](https://github.com/d3/d3-selection#selection_each) method on a selection allows you to invoke a function for each element selected. This is similar to how `map` or `forEach` work.
* Behind the scenes, for each element selected, `each` passes both the data associated with the element and the index of the element to the function. If 3 elements were selected, the first element selected would have a value of 0 for `i`.
* We haven't associated any data to these elements yet, so the value of `d` is undefined.
* `this` refers to the element itself (in case we wanted to use other D3 methods on the element).
* The [`data`](https://github.com/d3/d3-selection#selection_data) method allows you to bind data to selected elements. 
* The `data` method accepts an array of elements. If we pass fewer elements in this array than selected elements, not all elements will have data bound to them. If we pass more elements, we just ignore the extraneous elements.
* Calling the `data` method multiple times on a selection updates the data we associated with it prior. This process will be useful for updating data in charts later!
* After we've bound data to a selection, we can run other methods, e.g. `text`, to use that data to update the text of the element: `d3.select('ul').selectAll('li').text(d => d);`
* What if we don't have any elements on the page but want to bind data to those elements (e.g. I want to create new `li` elements for every piece of data in my array, where the text of that `li` element contains the data itself. Attempt #1 might look like: `d3.select('ul').selectAll('li').data([1, 2, 3, 4, 5]).append('li').text(d => d);`, but that doesn't work. We're just appending new `li` elements _within_ each existing `li` elements, and we don't get the 2 new elements we want (for 4 and 5).
* To get 5 `li` elements, each with the numbers 1 -> 5, two steps are required: 1.) `d3.select('ul').selectAll('li').data([1, 2, 3, 4, 5]).text(d => d);` to set the text of the existing elements to 1, 2, 3. Then `d3.select('ul').selectAll('li').data([1, 2, 3, 4, 5]).enter().append('li').text(d => d);` to create the two new elements.
* The `enter()` method is the key here: given selections and the associated data, `enter()` returns data that has not yet been bound to an existing element. In our case, we have 2 elements of our data array, 4 and 5, that aren't yet associated with any DOM elements. The methods that follow, like `append()`, get run for each of these _new_ elements of our data array.
* Running `enter()` on the selection first just adds two new elements, keeping the text of the existing elements the same. Why?
* The `exit()` method works in a similar way: if you've updated the data associated with your selections and now have fewer data elements than elements, you may need to _remove_ elements that no longer have data associated with them. After binding new data, you typically run `exit().remove()` to remove each of these elements from the DOM.
* Mike Bostock, creator of D3, wrote [a reference](https://bost.ocks.org/mike/join/) on this data-binding process.
* [One reference on data binding](https://www.sitepoint.com/a-beginners-guide-to-data-binding-in-d3-js/) that uses a gardening analogy.
* [A slightly more technical reference](http://alignedleft.com/tutorials/d3/binding-data) on data-binding.

#### Exercise 2 - Instructor Do More Data Binding (10 min)

* Here we're using Bootstrap to create an image gallery, but our HTML doesn't yet contain any images.
* Our `complexData` array contains objects as elements, each of which contains a title and a URL to an image.
* **We can bind this array of objects to selections, as well**.
* First, we select all `divs` within the element with the class `.img-gallery`. *This part is weird*: there are no `div` elements here, so the selection doesn't return anything. But this sets up the data binding and `enter()` method that follows to allow us to create new divs on this selection (a `div` for each element of data that hasn't been bound to data, which is all of our data). You can picture these initial `div` selections as creating "holes" in which we'll place our data when we run the `enter()` method.
* The `classed()` method accepts two arguments: a class or classes, and 2.) `true` or `false`. If `true`, we add the classes. If `false` we remove them.
* The `html` method sets the inner HTML of the element (the `div`) with whatever HTML we pass here.

#### Exercise 3 - Students Do D3 Table (15 min + 5 min review)

#### Exercise 4 - Everyone do Enter, Exit, Update (10 min)

* We're going to be manipulating the `div` elements within the outer `div` with an id of `content`.
* #1: We set the height of our divs to be proportional to the temperature.
* #2: Update only the new elements we get from the `enter()` method and the code that follows it.
* #3: Update only the _old_ elements. Since we never stored the result of our `enter()` code in its own variable, nor changed the style of the new `div` elements we created using that code, running `style()` on `selection` updates only the original elements tied to the selection (the original 3 elements).
* #4: We're seeing the [`merge()` method](https://github.com/d3/d3-selection#selection_merge) for the first time. This returns a new selection that combines the selection on which it's run (the new `div` elements we get from the `enter()` method) and the original selection we stored in the variable `selection`. This pattern is common: it merges all existing and new elements together, and allows us to run methods on that combined selection. **This lets us style every element at once**.
* #5: We're starting to combine everything we've learned together into one pattern now: style any new or existing elements with the pattern we saw above. For any elements in our selection that are no longer bound to data, remove them.
* #6: Finally, we can create a function that abstracts all of this logic. All we have to do is pass our array of data to it and it'll handle all of these updates for us!

#### Exercise 5 - Instructor Do SVG Elements (10 min)

* SVG = Scalable Vector Graphics
* SVG is an XML-based (looks a lot like HTML) image format for drawing 2-dimensional graphics that support interactivity and animation.
* All modern browsers include support for SVG.
* JPEG, GIF, and PNG are referred to as "bitmap" image formats. They are composed of individual pixels. As we scale those images, they tend to look blurry as a result. SVG images are composed of shapes, which scale as the dimensions of the overall image grow and shrink. See [this side-by-side](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics#/media/File:Bitmap_VS_SVG.svg) for a comparison.
* The `svg` element serves as a container for SVG shapes. We'll refer to the `svg` element as a "canvas". We must then include the actual shapes we want the browser to render within the `svg` element.
* The `rect` element tells the browser to render a rectangle. The `width` and `height` attributes 
* Elements are "painted" onto the canvas in the order in which they are appended. So the rectangle will be the first thing painted, then the circle on top of that, etc.
* Like other elements, we can apply CSS rules to SVG shapes.
* [List of all SVG elements](https://developer.mozilla.org/en-US/docs/Web/SVG/Element). Play around with some of the more obscure ones!
* The `svg` element itself can have width and height attributes.
* *Notice the `x` and `y` attributes for our rectangle*. Without these, our new shapes would be placed at (0, 0) in the SVG to which they're appended.
* To place the circle at a specific position, we use `cx` and `cy` (the (x, y) coordinates at the center of the circle).
* The `r` attribute of a circle sets the radius (in pixels).

#### Exercise 6 - Students Do SVG Stickman (10 min + 5 min review)

#### Exercise 7 - Everyone Do D3 Bullseye (10 min)

* We're going to create a bullseye with D3.
* We start out with an empty body. We'll be creating all of our elements, including our SVG, from scratch.
* `d3.select('body').append('svg')` creates our SVG.
* We can use the `attr` method to set the width and height of our SVG.
* We can append a `circle` element to our SVG and set all the attributes of the circle with `attr()`. Note that these aren't part of the `style` or CSS. They're part of the fundamental attributes of the element itself.
* Just like we did for our `li` and `div` elements before, we can bind data to circles and other SVG elements. We see the same pattern here as before, and we can still use functions within our D3 methods (here, with `attr()`) that run for each element we're operating on (every circle). Here we set the radius of the circle to the data bound to that circle.

#### Exercise 8 - Students Do Data Binding with Rectangles (10 min + 5 min review)

#### Exercise 9 - Students Do Upside Down Bar Chart (25 min + 10 min review)

#### Exercise 10 - Everyone Do Bar Chart Re-factored (10 min)
