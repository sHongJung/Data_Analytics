# Seek, Create, Update, and Destroy

## Instructions

* Import the `GlobalFirePower.csv` into a new table within a localhost database.

    * There is an error with the column headers that have been generated. They have spaces in them. Find a means by which to [**CHANGE**](https://stackoverflow.com/a/40866162) this so that they work properly.

    * Find all of those rows that have a "ReservePersonnel" of 0 and then remove these rows from the dataset.

    * Every country in the world at least deserves one "FighterAircraft". Only seems fair. Lets add one to each nation that has none.

    * Oh no! By updating this column, the values within "TotalAircraftStrength" column are now off for those nations! We've got to [add one](https://stackoverflow.com/a/2680352) to the original number.

    * A new nation has been founded and you are declared its leader! Congratulations! Unfortunately for you, every other nation is now looking to take over your land. Perform some calcuations to find the [Averages](https://www.w3schools.com/sql/sql_count_avg_sum.asp) for the "Total" columns, take note of them, and then set those as the values for your nation's military.

* **Bonus**:

    * After creating your new nation and some parts of your military strategies, go through each column in the newly created row and update their values in any way that you desire!
