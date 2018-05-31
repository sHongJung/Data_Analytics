// Creating our initial map object
// We set the longitude, latitude, and the starting zoom level
// This gets inserted into the div with an id of 'map'
var myMap = L.map('map', {
  center: [45.52, -122.67],
  zoom: 13,
});

// Adding a tile layer (the background map image) to our map
// We use the addTo method to add objects to our map
var access_token =
  'pk.eyJ1IjoiZHlsYnVyZ2VyIiwiYSI6ImNqaHNkZXpyYTAxdDAzcXJ6dzA3NHR5dXMifQ.oZt5CGSYffy4dZqIFSQciQ';
L.tileLayer(
  'https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?' +
    'access_token=' +
    access_token,
).addTo(myMap);
