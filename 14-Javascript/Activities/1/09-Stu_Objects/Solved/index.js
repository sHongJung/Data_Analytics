// Roster of player
var roster = [
  {
    name: "Doug",
    position: "Quarterback",
    madeTeam: true
  },
  {
    name: "Antonio",
    position: "Tight End",
    madeTeam: true
  },
  {
    name: "Nick",
    position: "Kicker",
    madeTeam: false
  },
  {
    name: "Ereck",
    position: "Offensive Live",
    madeTeam: false
  },
  {
    name: "AJ",
    position: "Line Backer",
    madeTeam: true
  }
];

// Counter for numberOfCuts
var numberOfCuts = 0;

// Log team
console.log("Your team this week:");
console.log("--------------");

// Loop through dictionary array
for (var i = 0; i < roster.length; i++) {
  var player = roster[i];

  // Print name and position for players on team
  if (player.madeTeam) {
    console.log(player.position + ": " + player.name);
  }
  // Add to numberOfCuts counters for players not on team
  else {
    numberOfCuts++;
  }
}
console.log("--------------");

// Print number of players cut
console.log(numberOfCuts + " players got cut.");
