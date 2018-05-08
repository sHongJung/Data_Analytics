// Create an object
var languages = {
  name: "Python",
  learn: true,
  weeks: [3, 4, 5, 6]
};

// JavaScript also allows value lookup via dot notation
console.log(languages.name);
console.log(languages.learn);
console.log(languages.weeks[0]);

// JS also allows value lookup via bracket notation--note the similarity to Python
// console.log(languages["name"]);
// console.log(languages["learn"]);

// Create an array of objects
var languagesArray = [
  {
    name: "Python",
    learn: true
  },
  {
    name: "SQL",
    learn: true
  },
  {
    name: "C++",
    learn: false
  }
];

// Loop through array of objects and print the value of the 'name' property for each one
for (var i = 0; i < languagesArray.length; i++) {
  // Retrieve the current language in the list
  var currentLanguage = languagesArray[i];

  // Log the value of the currentLanguage's name property
  console.log(currentLanguage.name);
}
