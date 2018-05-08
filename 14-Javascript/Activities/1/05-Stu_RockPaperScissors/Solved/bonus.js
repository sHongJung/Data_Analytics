// Randomly select the computer's choice
var computerSelections = ["r", "p", "s"];
var computerChoice = computerSelections[Math.round(Math.random() * 2)];
console.log("Computer: ", computerChoice);

// User Selection
var userChoice = prompt("Please choose (r)ock, (p)aper, or (s)cissors: ");
console.log("User: ", userChoice);

// alert choses
alert("The computer chose: " + computerChoice);
alert("You chose " + userChoice);

// conditionals to deteremine a winner
if (userChoice === "r" && computerChoice === "p") {
  alert("You Lose!");
}
else if (userChoice === "r" && computerChoice === "s") {
  alert("You Win!");
}
else if (userChoice === "r" && computerChoice === "p") {
  alert("Draw!");
}
else if (userChoice === "s" && computerChoice === "r") {
  alert("You Lose");
}
else if (userChoice === "s" && computerChoice === "p") {
  alert("You Win");
}
else if (userChoice === "s" && computerChoice === "s") {
  alert("Draw");
}
else if (userChoice === "p" && computerChoice === "s") {
  alert("You Lose");
}
else if (userChoice === "p" && computerChoice === "r") {
  alert("You Win");
}
else if (userChoice === "p" && computerChoice === "p") {
  alert("Draw");
}
else {
  alert("Invalid Input");
}
