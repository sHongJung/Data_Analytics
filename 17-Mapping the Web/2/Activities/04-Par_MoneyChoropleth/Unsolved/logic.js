// Creating map object
var myMap = L.map('map', {
  center: [40.7128, -74.0059],
  zoom: 11,
});

// Adding tile layer
L.tileLayer(
  'https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?access_token=' +
    'pk.eyJ1IjoiZHlsYnVyZ2VyMiIsImEiOiJjamh0dzZldGEwM25sM2trdDlkenBxam1tIn0.ln0RIf4CScMbTq-eYKKWyg',
).addTo(myMap);

// Link to GeoJSON
var APILink =
  'http://data.beta.nyc//dataset/d6ffa9a4-c598-4b18-8caf-14abde6a5755/resource/74cdcc33-512f-439c-' +
  'a43e-c09588c4b391/download/60dbe69bcd3640d5bedde86d69ba7666geojsonmedianhouseholdincomecensustract.geojson';

var geojson;

// Grabbing data with d3...
d3.json(APILink, function(data) {});
