// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");

// Start the table body with a blank HTML
$tbody.innerHTML = "";

// The outer loop fills the rows
// The inner loop fills the cells for each row
for (var i = 0; i < 100; i++) {
  // Insert a row into the table at position i
  var $row = $tbody.insertRow(i);
  // Insert five cells into the newly created row
  for (var j = 0; j < 5; j++) {
    var $cell = $row.insertCell(j);
    $cell.innerText = "Row " + (i + 1) + ", Cell " + (j + 1);
  }
}
