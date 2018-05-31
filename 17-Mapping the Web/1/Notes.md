## 17.1 - Map Visualizations with Leaflet

### Goals

* Learn the basics of creating map visualizations with Leaflet.
* Examine and understand the GeoJSON data format.

### Why?

* Map visualizations are critical for data-storytelling that involves geographic data.
* They are also really, really cool!

### Notes

* As always, the [Leaflet Docs](http://leafletjs.com/) are your friend!

### Exercises

#### Exercise 0 - Intro to Maps (5 min)

* This week, we'll be making maps with Leaflet, a JavaScript library, and Carto, an interactive tool for exploring maps. First two days are Leaflet, final day is Carto.
* [Mapping the spread of drought](https://www.nytimes.com/interactive/2014/upshot/mapping-the-spread-of-drought-across-the-us.html?_r=0)
* [Understand and predict Zika](https://carto.com/blog/understand-and-predict-zika-in-brazil/). This example uses Carto, a mapping tool we'll cover more in 17.3.
* [Spotify - Musical Map of the World](https://insights.spotify.com/us/2016/12/07/musical-map-of-the-world-2-0/)

#### Exercise 1 - First Map with Leaflet (Everyone Do - 15 min)

* Walk through this one with me. It'll be critical to the rest of the class, so we'll help get you set if you need support.
* [Leaflet.js](http://leafletjs.com/) is the primary library we'll be using to build map visualizations.
* Within our HTML file, we must include *both* the CSS and JS for Leaflet. The CSS includes icons and other markers we'll use in our maps later. See [this tutorial](http://leafletjs.com/examples/quick-start/) for links to the CSS / JS.
* Like with D3, we start with an empty div in our HTML file. This is where we'll insert our map.
* The file `logic.js` includes the JS code we'll use to create our map.
* With Plotly and D3, we used the global `Plotly` and `d3` objects to run the methods we needed. Here, loading the Leaflet JS gives us access to the `L` global object we'll use to create maps.
* `L.map()` accepts two arguments: 1.) the ID of the HTML element to which Leaflet should append the map, and 2.) an object containing properties about the map. In this case, we've provided it a `center` property (an array with two elements: the [lat, long] of the center of the map), and a "zoom level". Try changing both of these values later.
* `L.tileLayer()` accepts a URL that points us to a set of "tile layers", which form the background of our map. Mapbox is a mapping service that provides some of these tiles, so we're hitting a Mapbox URL here to grab the tiles we want. There are many types of tiles you can include, which will vary the way your map is displayed.
* Mapbox requires an `accessToken` of your own to hit their API to fetch tiles. When you create your own maps, you'll need to sign up for a free Mapbox account and create your own API key.
* After creating the tile layer, we immediately run the `addTo()` method of the tile object, which accepts a map object as an argument. This does what it says: adds the tile to the map we created above.
* **Sign up for a [Mapbox](https://www.mapbox.com/) account and [create an API key](https://www.mapbox.com/studio/account/tokens/)**.
* Finally, we'll need to add a bit of CSS to get our map to display. Setting a `height: 100%;` rule to `#map, body, html` selector is key here. Without this, our map will not display. `height: 100%` says: set the height to 100% of the height of the parent, so the rule must be applied to the parent of our `div` as well (`body` and `html`).

#### Exercise 2 - Adding Markers to our map (5 min)

* Markers allow us to identify specific places on our map using icons.
* [Leaflet Marker docs](http://leafletjs.com/reference-1.0.3.html#marker-option)
* `L.marker()` returns a Market object, which takes as arguments 1.) an array of [lat, long] coordinates on which we place the marker and 2.) an object of "options" tied to the marker.
* Just like with the tile layer above, we run `.addTo(myMap)` to add the marker to the map. This pattern (using the `addTo()` method) will become a theme.
* Marker objects have a `bindPopup()` method to attach a popup with HTML or some message. This popup appears on click.

#### Exercise 3 - Students Add Markers (15 min + 5 min review)

#### Exercise 4 - Other types of markers (10 min)

* We're not limited to the default marker icon, nor are we limited to just a pointer.
* *Key takeaway*: sometimes you want to highlight an area of a chart, or a range (with a line). You can do that with the variety of shapes Leaflet provides.
* `L.circle()` takes as arguments 1.) the center of the circle as an array of coordinates and 2.) an object that defines properties and styles of the circle (e.g. the radius, fill color, etc.)
* The Leaflet docs provide information on [all the Path options](http://leafletjs.com/reference-1.3.0.html#path) you can add to your chart.
* `L.polygon()` lets you create an arbitrary polygon.
* `L.rectangle()` lets you create a rectangle.

#### Exercise 5 - Students Review other types of markers (10 min + 5 min review)

#### Exercise 6 - Markers of Different Sizes (10 min)

* Key takeaway: just like with scatter plots, sometimes it makes sense to vary the size of our markers, so that markers reveal the magnitude of a key data point.
* Here, we create our own function `markerSize` that returns a number of *meters*. We divide by 40 only because the resulting number seems to get us a size that isn't too large or small.
* Since we can replace any fixed value with a function that returns a value of the same type (or any other expression that returns the same type), we can use our function to calculate the `radius` within our `L.circle` call.

#### Exercise 7 - Students make markers of different sizes (15 min + 5 min review)

#### Exercise 8 - Maps with Layers, Controls (10 min)

* So far we've only added one layer on our map. We can add multiple layers.
* For example, we want to add or remove markers from our map. If all of our markers are tied to a specific layer, we can toggle them all on and off.
* We can also toggle between different tile layers.
* The `layerGroup` method takes an array of markers, creating a layer of these markers that we'll use later.
* Here, our tile layers are considered "base layers" because they form the base of our map.
* We keep both of our base map layers inside of an object, with property names as the names of the layer we want to appear on our control panel (added in a moment).
* We then have a set of "overlay layers", which are overlayed on top of the base layers. These can be removed completely if we want.
* First, instead of progressively adding these layers onto our map with the `addTo()` method, we can provide a `layers` array in our initial map creation with `L.map()`. This expects an array of tile layer objects (above, we created each layer using `L.tileLayer()`.
* Finally, we can add a control to allow users to change these layers with the `L.control.layers()` method, which accepts 1.) the object of base layers and 2.) the object of overlay layers. See [this example](http://leafletjs.com/examples/layers-control/) in the Leaflet docs. We must add this to the map using the `addTo()` method.

#### Exercise 9 - Students do Layers (15 min + 5 min review)

#### Instructor Talks GeoJSON (5 min)

* GeoJSON is a data format that encodes geographic information (along with other metadata, e.g. the name of the place) in JSON string.
* [Example GeoJSON](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson)
* [GeoJSON is a _standard_](http://geojson.org/). Every GeoJSON document comes with specific object property names tied to the standard types of geography we'll encounter. e.g. Point, LineString, etc.
* Geographic features are contained within an array named `features`.
* Luckily, Leaflet parses these data for you.
* `L.geoJSON` creates a layer, taking as arguments 1.) the GeoJSON object that contains our data and optionally 2.) the object of options that specify how we process / style the GeoJSON layer.
* In this case, we have GeoJSON Point data. When processed with the `L.geoJSON()` method, we get back a layer of _markers_.
* [The Leaflet example on GeoJSON](http://leafletjs.com/examples/geojson/) has a lot more information about the `L.geoJSON` method.

#### Exercise 10 - Students Do GeoJSON (15 min + 10 min review)
