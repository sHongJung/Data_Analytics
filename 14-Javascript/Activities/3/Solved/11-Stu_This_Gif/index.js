// Add button click event
d3.selectAll("button").on("click", function() {

  // Grab name from button clicked
  var person = d3.select(this).attr("data-person");
  console.log(person);

  // Construct API query URL
  var queryURL = "https://api.giphy.com/v1/gifs/search?q=" +
      person + "&api_key=dc6zaTOxFJmzC&limit=10";
  console.log(queryURL);

  // Make API request
  d3.json(queryURL, function(error, response) {

    // Handle errors
    if (error) return console.warn(error);

    // Grab response
    var results = response.data;
    console.log(results);

    // Loop through response
    for (var i = 0; i < results.length; i++) {
      if (results[i].rating !== "r" && results[i].rating !== "pg-13") {
        // Rating
        var rating = results[i].rating;
        console.log(rating);

        // Image
        var image = results[i].images.fixed_height.url;
        console.log(image);

        // append a div with class item
        var gifDiv = d3.select("#gifs-appear-here")
                          .append("div")
                          .attr("class", "item");

        // Append a paragraph with rating
        gifDiv.append("p").text("Rating " + rating);

        // Append an image to div
        gifDiv.text("Rating: " + rating).append("img").attr("src", image);
      }
    }
  });
});
