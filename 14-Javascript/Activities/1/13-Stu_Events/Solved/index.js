// Set variable for the button
var buttonClick = document.querySelector("#clickHere");

// Add click even listener to the button
buttonClick.addEventListener("click", function() {
  // Prompt user for favorite color
  var favoriteColor = prompt("What is your favorite color? ");

  // Create paragraph element
  var colorText = "Your favorite color is " + favoriteColor + ".";

  // Select the id tag for color
  var color = document.querySelector("#color");

  // Add new html line to color
  color.innerHTML = colorText;
});
