// Creating map object
var map = L.map('map', {
  center: [40.7128, -74.0059],
  zoom: 11,
});

// Adding tile layer
L.tileLayer(
  'https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?' +
    'access_token=pk.eyJ1IjoiZHlsYnVyZ2VyMiIsImEiOiJjamh0dzZldGEwM25sM2trdDlkenBxam1tIn0.ln0RIf4CScMbTq-eYKKWyg',
).addTo(map);

var link =
  'http://data.beta.nyc//dataset/0ff93d2d-90ba-457c-9f7e-39e47bf2ac5f/resource/' +
  '35dd04fb-81b3-479b-a074-a27a37888ce7/download/d085e2f8d0b54d4590b1e7d1f35594c1pediacitiesnycneighborhoods.geojson';

// Our style object
var mapStyle = {
  color: 'white',
  fillColor: 'pink',
  fillOpacity: 0.5,
  weight: 1.5,
};

// Grabbing our GeoJSON data..
d3.json(link, function(data) {
  // Creating a geoJSON layer with the retrieved data
  L.geoJson(data, {
    // Passing in our style object
    style: mapStyle,
  }).addTo(map);
});
