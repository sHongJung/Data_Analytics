# DataStorms

In this activity, students will practice applying `group_by` and `summarise` to analyze storm frequency data.

## Instructions

* Make a table of how many days per month had a category 3+ storm before 1990.

* Make a table of how many days per month had a category 3+ storm during and after 1990.

* From the storms dataset in dplyr (accessible via `dplyr::storms`), give the _median pressure_ and the _range of pressures_ for each year

* Give the mean and median pressure by year and name. Only select storms that were hurricanes.

* Generate a tibble with groups for _both_ `year` _and_ `status`. Create a summary contaiing unique storm names. 

* Give the number of category 4+ storms that happened each year, and calculate the average month per year that a category 4+ hurricane has happened.

  * Take into account the days and hours of the of the month when accounting for the mean month of the storms.
