## 17.2 - More GeoJSON, Leaflet Plugins

### Goals

* Get a firm grasp of GeoJSON and the associated Leaflet methods for working with GeoJSON data.
* Learn about the [Leaflet plugin ecosystem](http://leafletjs.com/plugins.html), implement visualizations using some of these plugins.
* Gain more experience reading the Leaflet / Leaflet plugin docs.
* Write a lot of code!

### Exercises

#### Review GeoJSON (10 min)

* GeoJSON is a data format that encodes geographic information (along with other metadata, e.g. the name of the place) in JSON string.
* [Example GeoJSON](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson)
* [GeoJSON is a _standard_](http://geojson.org/). Every GeoJSON document comes with specific object property names tied to the standard types of geography we'll encounter. e.g. Point, LineString, etc.
* Geographic features are contained within an array named `features`.
* Luckily, Leaflet parses these data for you.
* `L.geoJSON` creates a layer, taking as arguments 1.) the GeoJSON object that contains our data and optionally 2.) the object of options that specify how we process / style the GeoJSON layer.
* In this case, we have GeoJSON Point data. When processed with the `L.geoJSON()` method, we get back a layer of _markers_.
* [The Leaflet example on GeoJSON](http://leafletjs.com/examples/geojson/) has a lot more information about the `L.geoJSON` method.

#### Exercise 1 - NY Neighborhoods (20 min)

This exercise slowly builds up the features of our map. There are 4 separate JS files, and we'll be switching between them as we move through each part.

Part 1 - `logic.js`

* We use `d3.json()` to fetch our GeoJSON file, adding it to our map with `L.geoJSON(data).addTo(map)`.
* In the first case, this GeoJSON file contains a map of the neighborhoods of New York City.
* Note that there's a default `fillOpacity` on the layer. We can control this and other options by passing in our Options object to the `L.geoJSON()`, e.g. `L.geoJSON(data, { fillOpacity: 0.8 })`.

Part 2

* Here, we want to apply a custom style to our layer.
* We add an Options object that includes a `style` property, which allows us to pass a variety of properties that lets us apply custom styles to our layer.

Part 3

* This part is going to be really cool.
* We want to vary the color of the GeoJSON features based on the borough, which is included in the GeoJSON file.
* Within the Options object, we can add a function as the value of the `style` property (we can put a function that returns an object anywhere an object is expected).
* The `L.geoJSON()` method will pass in the current feature it's currently processing as an argument to this function, so we can use that here to style our features based on properties of the feature in the GeoJSON file (see the GeoJSON file)
* To color the feature based on the borough, we pass the borough to a `chooseColor` function, which simply returns a string of the color we want to assign to the feature based on the current borough.

Part 4

* Here, we want to add event listeners to add some interactivity to our chart (on mouseover and mouseout). We also want to add some zoom effects and popups.
* There's a lot more going on here, not all of which you might understand the first time. That's OK.
* The `onEachFeature` property we pass to our Options object allows us to run a function on each feature (and associated portion of our layer).
* The `L.geoJSON()` method passes the current feature and layer to the function so that we can add events, popups, etc. to the layer
* Similar to how we added event listeners to elements in D3, Leaflet uses the `on()` method to add event listeners to layers. 
* Here, we want to add multiple event listeners, so we can pass an object with the event names as keys and the callback function as the value, e.g. `{ mouseover: function(event) { console.log('user moused over this element!') } }`. This lets us easily add multiple event listeners at the same time. [The docs](http://leafletjs.com/reference-1.3.0.html#evented-on) have more information about this.
* Within each of these callback functions we reference `event.target`, which is the layer the user currently interacted with. Given a layer, we can change the style of the layer with code like `layer.setStyle({ fillOpacity: 0.5 })`
* On `click`, we implement zoom behavior with `map.fitBounds()`, which takes as an argument the boundaries of the element the user clicked, zooming in on that space.
* Finally, we use the `bindPopup()` method of our layer to set the text of the popup that will also appear on click.

#### Exercise 2 - Introduction to Leaflet Plugins (15 min)

* Leaflet plugins extend the core functionality of the library.
* [Leaflet Plugins Page](http://leafletjs.com/plugins.html)
* We'll be using [this data set](https://data.sfgov.org/Public-Safety/Map-of-Police-Department-Incidents/gxxq-x39z) for this particular visualization.
* `just-crime.html` creates a marker for each incident in the dataset. This is too much to make sense of. What other visualizations might help us better summarize these data?
* We'll use the [Leaflet.heat heatmap plugin](https://github.com/Leaflet/Leaflet.heat) to create a heatmap of the crime data.
* A heatmap works by creating points, each with a given radius. If we have points whose radii overlap, that overlapping section will be colored a deeper hue of red. So areas where we have more overlapping points will be deep red, and areas that have few overlapping points will be closer to green (generally). See [this technical reference](http://cartographicperspectives.org/carto/index.php/journal/article/view/cp80-deboer/1420) on heatmaps for more information.
* We created the `leaflet-heat.js` JavaScript file separately, and must include that in the `head` of our HTML in order to use it.
* The heatmap plugin gives us an `L.heatLayer()` method that accepts an array of (lat, long) pairs and creates a heatmap layer from the density of those points.
* Note that these plugins extend the functionality of the global Leaflet object (`L`), so using the plugin is as easy as just using a new Leaflet method on the `L` object.

#### Exercise 3 - Students Do Rat Cluster (30 min + 10 min review)

* Socrata (the technology that powers the NY OpenData Portal) [provides a UI](https://dev.socrata.com/foundry/data.cityofnewyork.us/fhrw-4uyv) that lets you build a query URL from the available parameters, so you can filter your dataset.

### LUNCH

#### Exercise 4 - Choropleth (30 min + 10 min review)

* [Choropleths](https://en.wikipedia.org/wiki/Choropleth_map) are like heatmaps but for geographic data.
* "The difference here would be that the choropleth’s generated data will be by a non-regular enumeration unit that makes sense to people like countries, states, watersheds, counties or census blocks. A heat map would be depicted across a regular grid of cells, their size specified by the cartographer, but in any case, uniformly calculated." - from [this reference](http://www.gretchenpeterson.com/blog/archives/2694).

#### Exercise 5 - Make your own maps! (30 min)

* Divide into groups of 4 (some groups may have +/- 1)
* We'll have as many groups as possible give a very brief (2 - 3 min) presentation afterwards!
* Use [this reference on how to make good map visualizations](https://onlinejournalismblog.com/2015/08/24/when-to-use-maps-in-data-visualisation-a-great-big-guide/)
