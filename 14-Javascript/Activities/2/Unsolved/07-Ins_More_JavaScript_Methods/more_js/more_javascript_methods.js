// #1. Methods to access an objects keys and/or values

// An array of objects
var people = { mom: "wilma flintstone", dad: "fred flintstone", daughter: "pebbles", son: "bambam" };

// Display the entire object, both keys and values
console.log(people);

// Display only the keys of the object
console.log(Object.keys(people));

// Display only the values of the object
console.log(Object.values(people));

// Display a 2D Array holding Arrays of ['key', 'value']
console.log(Object.entries(people))

// #2. filter()
// Another array of objects, representing a cartoon family
var simpsons = [{ name: "Homer", age: 45 }, { name: "Lisa", age: 8 }, { name: "Marge", age: 43 }, { name: "Bart", age: 10 }, { name: "Maggie", age: 1 }];

function selectYounger(person) {
  return person.age < 30;
}

var youngSimpsons = simpsons.filter(selectYounger);

console.log(youngSimpsons)



