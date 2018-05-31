# Unit 17 Outline

### Homework Description

* In this unit, students will use leaflet.js along with data from the USGA to visualize earthquake data.

### Key Concepts

* Importance // Uniqueness of Geo-Visualization
* Utilizing External Leaflet Plugins
* Understanding GeoJSON
* Gathering Data & Advanced API Consumption (URL Parameters)

### Rough Outline

* Day 1 - Intro & Basic Leaflet:

  * Introduction to Geo-Visualization & Leaflet // CARTO
    * What insights does Geo-Mapping give us over looking at 'flat-data'?
      * Drought Example
      * Zika Containment Example
      * Spotify Map
  * Give students a bit of time to look over the leaflet site // documentation
  * Getting our first map onto the page (code along with the instructor)
    * Linking to leaflet libraries // setting up HTML page
    * Creating a Mapbox account and grabbing a tile-layer
    * Styling the map on the page
    * Dissect // walk-through basic leaflet map code
      * Map Object, setView method, zoom, tileLayer, adding things to map with the addTo method
  * Playing around with basic map (Change zoom, starting coordinates, background tile-set)
    * Exercise where students find their coordinates and change the map to start/zoom on them + change map tile-set
  * Adding a marker to the map
    * Changing properties of a marker
    * Student exercise plotting cities (NY, LA, etc..) on the map.
  * Advanced Marker Properties
    * Tool-tips, Events, Pop-ups
  * Students Do - Exercise with markers & pop-ups
  * Other types of markers (Circles, Lines, Polygon, etc...)
    * Custom styling of markers
    * Exercise plotting cities with style based on their population
  * Layers (Layer Groups // Controls // Base Maps)
    * Instructor does simple layer // base map example
      * Example where multiple layers helps to illustrate something? - Plot data from 3 different time periods
          (Expansion of Walmart? Spill Data?)
    * Students break apart previous city example into layers.
  * Longer Example Pulling Concepts Together

* Day 2 - Advanced Leaflet:

  * Review from yesterday
    * Warm up exercise.
    * Create new map, plot markers // polygons on different layers.
  * Setting Custom Icons
    * Take the previous example and change capitol cities to a different icon.
    * Plotting
  * Sourcing Data
  * Grabbing data from the Data.gov // OpenNYC API
    * Instructor Example
    * Student Exercise
  * API calls and plotting data with Leaflet.
    * Student Exercise 
  * GeoJSON 
    * What is it?
    * Instructor Example - Adding to map with API
  * Basic Student GeoJSON exercise
  * GeoJSON - Styling // onEachFeature // filter function - Changing feature/marker styling based on properties
  * More involved student exercise
  * Using plugins to create advanced visualizations
    * Instructor simple demo followed by student simple example
    * Harder // more involved example
    * Clustering // Heatmap

* Day 3 - Using CARTO & Leaflet Group Work
  * Introduction to CARTO
    * Students create accounts and explore site // CARTO Gallery
  * What is GeoJSON? (move to 17.2)
  * Our first CARTO map (McDonald's Example)
    * Creating a CARTO map // Importing & Viewing Data
    * Navigating the CARTO UI // Wizards
    * Different visualizations & how they are effective at showing different things.
  * Customizing our CARTO map
    * Utilizing CARTO CSS
  * Intro to CARTO SQL
  * CARTO SQL and Geospatial Queries (Needs to be expanded upon // explained more from previous lesson).
  * Choropleth Activity
    * Importing & merging different types of data
    * Styling
  * Deploying maps (to HTML)
  * Student CARTO exercise with their own dataset
  * Long leaflet.js build possibly w/ partners or small groups.
    * Maybe keep the Citibike example. Simplify // clean up.
