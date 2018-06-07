### Goals

* Further develop Leaflet skills.
* Understand how to create basic maps with CARTO, a UI for creating and interacting with maps.
* Spend some time reviewing anything y'all want to go over.

### Why?

* CARTO is powerful because it gives us a tool that faciliates the creation and analysis of maps. **We often want to use the tool that gets the job done with the least amount of code**, since it's faster to work with and less complex to maintain.

### Notes

* Remember to keep your Mapbox API key handy so that you can use it for these exercises.

### Exercises

#### Exercise 1 - Students Do More Leaflet with Citi Bike (10 min intro, 40 min to work on exercise, 10 min review)

* You'll be using Leaflet to create a map that visualizes data from the City Bike API (NYC).
* There's a Basic and an Advanced version. Start with the Basic, and if you finish, work on the Advanced.
* We're using [this dataset](https://gbfs.citibikenyc.com/gbfs/en/station_information.json).
* The Basic version includes a standard marker with a popup that lists the name and the capacity of bikes available at each station.
* The Advanced version additionally includes the number of bikes currently available.
* The Advanced version uses a plugin (you can pick your own, but we suggest one you should look at) that attaches a unique icon to each type of station.
* The Avdanced version also includes a legend at the bottom right indicating how many of each type of station are included in the whole map.
* **This is a very ambitious exercise and do not worry if you don't finish**. If you don't, this is a good exercise to work through on your own time.
* [Reference on the `new` keyword](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)

#### Introduction to CARTO, Account Creation (10 min)

* [CARTO](https://carto.com/) is a UI for building and interacting with maps, minimizing the code it takes to create them. You can build a map without any code, but customization requires a bit of it.
* You may see references to CartoDB, the former name of the tool (very recently renamed).
* CARTO changed more than just its name recently. Parts of it were rebuilt to faciliate the creation of maps for non-developers (before, it was a bit harder for the non-technical to work with).
* **Go to [carto.com](https://carto.com/) to create a new account**.
* Free for 30 days, paid after that. There is a [student program](https://carto.com/community/ambassadors/) I haven't explored.

#### Everyone Do - Creating our first CARTO map (15 min)

* CARTO will accept a variety of file formats, as long as it can find the relevant geographic data to plot. The type of data CARTO can accept is described [here](https://carto.com/docs/carto-engine/import-api/importing-geospatial-data/).
* Take the McDonalds CSV in the `Resources` directory for this exercise and upload it to create a new map.
* CARTO can also accept Shapefiles, which you may encounter in your work with geographic data. In general, if it's geographic data, CARTO can likely deal with it, or you can easily turn it into a format that CARTO can deal with.
* First, **play around** with the UI.
* Clicking on the icon next to the dataset name allows us to edit features of the data, style our map, change the aggregation, and much more.

#### Everyone Do - Customizing our CARTO map (10 min)

* In the `STYLE` tab of our Carto map options, toggle the button near the bottom-left of the map from "VALUES" to "CARTOCSS".
* CARTOCSS is what's referred to as a CSS "preprocessor". This isn't normal CSS. You can't take this and export it to use in your own map. But Carto provides a language that looks similar to CSS that allows you to tailor specific styles of your map with a single line of code that would normally take many more. So it facilitates the styling of maps.
* `marker-width`: the width of the marker
* `marker-fill`: the fill color of the marker
* `marker-fill-opacity`: a value of 1 indicates the marker is completely opaque, 0 completely transparent.
* `marker-allow-overlap`: `true`: allow overlapping markers. `false`: overlapping markers will not show up until you zoom in.
* [The docs on CARTOCSS](https://carto.com/docs/carto-engine/cartocss/)
* We can style our markers by value, e.g. by state, by clicking on the point color under the "STYLE" tab, clicking the "BY VALUE" option, selecting the relevant field and choosing the color format from there.

#### Everyone Do - CARTO SQL (10 min)

* Under the "DATA" tab tied to our layer, switch the toggle near the bottom-left from "VALUES" to "SQL".
* When we upload our data, CARTO loads that data into a PostgreSQL database table behind the scenes (PostgreSQL is a lot like MySQL, but has better support for geographic data / queries). Therefore, we can query the data in this DB table to display a certain set of results!
* We can always see the results of our query in a table format if we toggle the map view to the "DATA" view in the bottom-right corner of the map.

### REVIEW
