// Assign green button to a variable
var $btn = d3.select("#green-button");

// Assign red button to a variable
var $transform = d3.select("#red-button");

// D3 event handler
$btn.on("click", function clickHandler() {
  // Append a panel div to the page
  var newPanel = d3.select(".main").append("div");
  // Assign class to the panel
  newPanel.attr("class", "panel panel-warning");

  // Append a panel body to the panel
  var newSubPanel = newPanel.append("div");
  // Assign class to the subpanel
  newSubPanel.attr("class", "panel-body");
  // Assign text to the element
  newSubPanel.text("Hello from the outside");
});

// D3 event handler
$transform.on("click", function clickHandler() {
  // Select all elements of a class
  d3.selectAll(".panel-body")
    // Change the text
    .text("Goodbye for now")
    // Set its class
    .attr("class", "goodbye")
    // Set its class again
    .attr("class", "panel-body")
    // Change the font-size
    .style("font-size", "20px")
    .style("background", "green");
});
