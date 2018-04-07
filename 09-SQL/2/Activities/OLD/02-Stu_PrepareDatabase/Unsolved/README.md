# Prepare the Database

This activity allows students to prepare a schema for importing a massive CSV file. 

## Instructions

* It's time to test your skills in creating databases and tables as you create a database called `top_songsDB`, which will eventually house all of the music data contained within `TopSongs.csv`.

  * Within your database create a table called `Top5000` and create columns capable of holding all of the data contained within `TopSongs.csv` properly.

  * All of your code should be written and saved within a filed called `schema.sql` so that you can use this same code later should the need ever arise.

  * Columns you will need are: **artist name**; **song name**; **year**; **raw popularity score** for the song from the entire world; and then one column for each of the **raw popularity scores** for the song from the USA; UK; Europe (i.e., non-English speaking countries in Europe); and the rest of the world, respectively.

  * Pay particular attention to the data types that your columns will require. For example, which data type will the first column require? What about the last column?

## Bonuses

* Create a `seeds.sql` file that contains queries for inserting the first three songs found within `TopSongs.csv`.

* Look into how MySQL Workbench can import and export data files. What file types does it accept? How does it convert the data?

## Hints

* Look up the data type used in MySQL to store decimals. Try the [MySQL documentation](https://dev.mysql.com/doc/) and search for "data types."

* We have also included an exact [reference](https://dev.mysql.com/doc/refman/5.7/en/numeric-types.html), but we encourage you to improve your skills in consulting documentation whenever possible!
