//Part I
// A function that responds 'Polo!' if it hears 'Marco'
function marcoPolo(heardWord) {
  if (heardWord.toLowerCase() === "marco") {
    return "Polo!";
  }

  return "Try again!";

}

marcoPolo("Marco");


//Part II
// A function that uses a callback function to respond to a message
// `hollaBack` is the callback function here
function respond(heardWord, hollaBack) {
  return hollaBack(heardWord);
}

// A function that responds 'Polo' if it hears 'Marco'
// This function corresponds to the `hollaBack` callback function
function marcoP(word) {
  if (word.toLowerCase() === "marco") {
    return "Polo!";
  }

  return "Try again!";

}

// Call the function with the arguments 'marco' and marcoP()
respond("marco", marcoP);
// Call the function with the arguments 'jessica' and marcoP()
respond("jessica", marcoP);
