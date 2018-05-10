// Getting references to the input fields, button, and lists
var $nameInput = document.querySelector("#name");
var $ageInput = document.querySelector("#age");
var $submitBtn = document.querySelector("#submit");
var $cannotWatchList = document.querySelector("#cannot-watch");
var $canWatchList = document.querySelector("#can-watch");

// When the submit button is clicked, call the handleSubmitClick function
$submitBtn.addEventListener("click", handleSubmitClick);

function handleSubmitClick(event) {
  // The default behavior of a button clicked inside of a form is to try to submit the form somewhere (which we don't want)
  event.preventDefault();

  // Create a new movie patron object that will hold the data used to populate the page
  var newMoviePatron = {
    name: $nameInput.value.trim(),
    age: $ageInput.value.trim()
  };

  // Clearing the input fields
  $nameInput.value = "";
  $ageInput.value = "";

  if (newMoviePatron.age < 17) {
    var $li = document.createElement("li");
    $li.className = "list-group-item";
    $li.innerText = newMoviePatron.name;
    $cannotWatchList.appendChild($li);
  }
  else {
    $li = document.createElement("li");
    $li.className = "list-group-item";
    $li.innerText = newMoviePatron.name;
    $canWatchList.appendChild($li);
  }
}
