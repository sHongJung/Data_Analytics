//  Calling the renderHTML function
renderHTML();

function renderHTML() {
  // Getting a reference to the element on the page with an ID of app
  var app = document.querySelector("#app");

  // Storing a string into a variable
  var headingMessage = "The 'document.querySelector' Method";

  // Storing a string into the paragraphMessage variable.
  var paragraphMessage = "The 'document.querySelector' method allows us to get a reference to an element in the DOM and store it into a variable. ";
  paragraphMessage += "There are a variety of properties we can set on DOM elements, one of which is called 'innerHTML'. ";
  paragraphMessage += "The innerHTML property allows us to update the HTML content of an element.";


  // Create a heading element w/ document.createElement
  var heading = document.createElement("h1");
  var paragraph = document.createElement("p");

  // Update the innerHTML property of these elements
  heading.innerHTML = headingMessage;
  paragraph.innerHTML = paragraphMessage;

  // Use 'appendChild' to put the heading and paragraph into the `app` container
  app.appendChild(heading);
  app.appendChild(paragraph);
}
