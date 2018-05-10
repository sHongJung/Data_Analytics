// Reference the counter text element on the page by its ID
var $count = document.getElementById("counter");
// Reference the Increment and Decrement buttons by their classes
var $incrementBtn = document.querySelector(".panel .btn.btn-primary");
var $decrementBtn = document.querySelector(".panel .btn.btn-danger");

// Add click event listeners to the buttons, call the functions passed in
$incrementBtn.addEventListener("click", handleIncrementClick);
$decrementBtn.addEventListener("click", handleDecrementClick);

// Initialize the count at 0
var count = 0;
// Initialize colors at 0
var red = 0;
var blue = 0;
// Initialize fontSize at 40
var fontSize = 40;

// Render the count value to the page for the first time when it loads
renderCount();

function renderCount() {
  // Update the inner text of the $count element
  $count.innerText = count;
  // Update the font color of the $count element
  $count.style.color = "rgb(" + red + ", 0, " + blue + ")";
  // Alternatively, you can use template literals for a cleaner look
  // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals
  // $count.style.color = `rgb(${red},${0},${blue})`;  
  // Update the font size of the $count element
  $count.style.fontSize = "" + fontSize + "px";
  // $count.style.fontSize = `${fontSize}px`
}

// handleDecrementClick decreases count by 1 and re-renders the count to DOM
// Also changes red and blue rgb values by 40
function handleDecrementClick() {
  // Decrease the counter number by two
  count -= 2;
  // Increase red by 40 and decrease font size by 2px; decrease blue by 40
  red += 40;
  blue -= 40;
  fontSize -= 2;
  renderCount();
}

// handleIncrementClick increases count by 1 and re-renders the count to DOM
// Also changes red and blue rgb values by 40
function handleIncrementClick() {
  count += 2;
  // Decrease red by 40 and increase font size by 2px; increase blue by 40  
  red -= 40;
  blue += 40;
  fontSize += 2;
  renderCount();
}

