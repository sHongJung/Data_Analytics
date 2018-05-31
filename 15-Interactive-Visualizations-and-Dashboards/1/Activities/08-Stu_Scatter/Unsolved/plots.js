// YOUR CODE HERE
var Trace1 = {
  x: data.year,
  y: data.high_jump,
  name : "High_Jump",
  mode:"markers",
  marker :
  {
    symbol : "dot"
}
};

var Trace2 = {
  x: data.year,
  y: data.discus_throw,
  name : "Discus_Throw",
  mode: "markers",
  marker:
  {
    symbol :"triangle-up"
}
};

var Trace3 = {
  x: data.year,
  y: data.long_jump,
  name : "Long_Jump",
  mode:"markers",
  marker :
  {
    symbol :"diamond-wide-dot"
  }
};

data = [Trace1, Trace2, Trace3];

layout = {
  title : "Olympics",
  xaxis : {
    title: "year"
  },
  yaxis : {
    title:"inches"
  }
};

Plotly.newPlot("plot", data, layout);
