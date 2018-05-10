# Click Counter Demo

In this activity we will review basic concepts covered in the previous like such as referencing DOM elements in our JavaScript code, listening for events, and manipulating the DOM with JavaScript.

## Instructions

1. Open [index.html](index.html) in your web browser and take a moment to understand the app's functionality: The number displayed increases by one when the `Increment` button is clicked, and decreases by one when the `Decrement` button is clicked.

2. Open [index.js](index.js) and study the code. First we get references to the `h1` tag displaying the click count, as well as the `Increment` and `Decrement` buttons.

3. Then we add click event listeners to `$incrementBtn` and `$decrementBtn` and pass in `handleIncrementClick` and `handleDecrementClick` to handle the click events.

4. We initialize a count variable at `0` and run the `renderCount` function which sets the inner text of the `$count` element to be equal to the count variable.

5. Below, `handleIncrementClick` and `handleDecrementClick` are defined. These functions are called in response to `$incrementBtn` or `$decrementBtn` being clicked. The count value is increased or decreased by `1` depending on which function runs.

6. `renderCount` is called after each change to the `count` variable, which updates the page.
