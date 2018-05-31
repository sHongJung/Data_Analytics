var trace = {
  x: [0, 1, 2, 3, 4],
  y: [0, 1, 2, 3, 4],
  type: 'scatter',
};

var trace2 = {
  x: [0, 1, 2, 3, 4],
  y: [0, 1, 4, 7, 4],
  type: 'scatter',
  line: {
    color: 'red',
  },
};

var layout = {
  title: 'My awesome chart',
};

var data = [trace, trace2];

Plotly.newPlot('myPlot', data, layout);
