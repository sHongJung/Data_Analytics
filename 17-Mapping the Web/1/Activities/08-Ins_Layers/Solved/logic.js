// An array of cities and their locations
var cities = [
  {
    name: 'Paris',
    location: [48.8566, 2.3522],
  },
  {
    name: 'Lyon',
    location: [45.764, 4.8357],
  },
  {
    name: 'Cannes',
    location: [43.5528, 7.0174],
  },
  {
    name: 'Nantes',
    location: [47.2184, -1.5536],
  },
];

// An array which will be used to store created cityMarkers
var cityMarkers = [];

for (var i = 0; i < cities.length; i++) {
  // loop through the cities array, create a new marker, push it to the cityMarkers array
  cityMarkers.push(
    L.marker(cities[i].location).bindPopup('<h1>' + cities[i].name + '</h1>'),
  );
}

// Add all the cityMarkers to a new layer group.
// Now we can handle them as one group instead of referencing each individually
var cityLayer = L.layerGroup(cityMarkers);

// Define variables for our tile layers
var light = L.tileLayer(
  'https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?' +
    'access_token=pk.eyJ1IjoiZHlsYnVyZ2VyIiwiYSI6ImNqaHNkZXpyYTAxdDAzcXJ6dzA3NHR5dXMifQ.oZt5CGSYffy4dZqIFSQciQ',
);
var dark = L.tileLayer(
  'https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?' +
    'access_token=pk.eyJ1IjoiZHlsYnVyZ2VyIiwiYSI6ImNqaHNkZXpyYTAxdDAzcXJ6dzA3NHR5dXMifQ.oZt5CGSYffy4dZqIFSQciQ',
);

// Only one base layer can be shown at a time
var baseMaps = {
  Light: light,
  Dark: dark,
};

// Overlays that may be toggled on or off
var overlayMaps = {
  Cities: cityLayer,
};

// Create map object and set default layers
var myMap = L.map('map', {
  center: [46.2276, 2.2137],
  zoom: 6,
  layers: [light, cityLayer],
});

// Pass our map layers into our layer control
// Add the layer control to the map
L.control.layers(baseMaps, overlayMaps).addTo(myMap);