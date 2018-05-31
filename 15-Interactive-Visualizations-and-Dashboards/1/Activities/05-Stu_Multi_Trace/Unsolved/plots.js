//console.log(data);
// YOUR CODE HERE
// Create our first trace
//
// greekN = [];
// greekR = [];
// romanN = [];
// romanR = [];
//
// var = i;
// for(i=0, i < data.length, i++) {
// greekN.push(data[i]['greekName']);
// greekR.push(data[i]['greekSearchResults']);
// romanN.push(data[i]['romanName']);
// romanR.push(data[i]['romanSearchResults']);
// };

var trace1 = {
  x: data.map(row => row.pair),
  y: data.map(row => row.greekSearchResults),
  name : "Greek",
  type: "bar"
};

// Create our second trace
var trace2 = {
  x: data.map(row => row.pair),
  y: data.map(row => row.romanSearchResults),
  name : "Roman",
  type: "bar"
};

// The data array consists of both traces
var data = [trace1, trace2];

// Note that we omitted the layout object this time
// This will use default parameters for the layout
Plotly.newPlot("plot", data);
