// @TODO: Complete the following sections

//console.log(data);
// Sort the data array using the greekSearchResults value
data.sort(function(a, b) {
   // resulting order is (3, 2, -120)
  return a.greekSearchResults - b.greekSearchResults;
});

//console.log(data);


// Slice the first 10 objects for plotting

sliceData = data.slice(0,10);
sliceData = sliceData.reverse();
console.log(sliceData);

// Trace1 for the Greek Data
var Trace1 = {
  x: sliceData.map(row => row.pair),
  y: sliceData.map(row => row.greekSearchResults),
  name : "Greek",
  type: "bar",
  orientation : "h"
};

// set up the data variable
var data = [Trace1];

// set up the layout variable
var layout = {
  title : 'Greek Data',
  xaxis : {
  title: 'Pair',
},
  yaxis : {
  title: 'greekSearchResults'
},
  margin : {
    l: 100,
   r: 100,
   b: 100,
   t: 100
  }
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", data, layout);
