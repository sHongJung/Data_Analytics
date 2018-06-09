# Filtering and Selecting

## Objective

The goal of this exercise are to do the following
1. Briefly show students how to inspect `tibbles` through theuse of `head()` and `tail()`.
2. Demonstrate Selecting columns of data for analysis
3. Demonstrate function piping in the context of `tibbles`
4. Demonstrate filtering data through the use of the `tidyverse` and more specifically `dplyr`

> **NOTE:** The bullet points match the order of the examples in the exercise

## Inspect the `Tibble`

* Use of `head()` shows the first 10 records
* Use of `tail()` shows the last 10 records.
* Use of `print(n=)` allows the user to print as many rows as they would like from the begining of the `tibble`.
* Using the argument `n=` allows the user more granular control to dertermine how many rows that they would like to see from `head()`, `tail()`, or `print()`

## Selecting and Renaming columns

> `select()` allows you to choose only the columns that you want to proceed with for your analysis

* Selecting only `Major.Min.Comp` and `Appraisal` demonstrates that the resst of the columns are ommited
* Using `-` in front of `Mass` demonstrates that only `Mass` is let out of the selection
* Columns can be selected by index
* They can also be ommited by intex; note that to do this `()` are needed around the indicies

  > `dplyr` provides some functions that can only be used within the context of `select()`. A few of these are `starts_with()`, `ends_with()`, `contains()`, and `everything()`

* Using `starts_with()` or `ends_with()` allows you to bulk filter for columns that match your starting or ending criteria
* Using `contains()` allows you to bulk filter for column names that contain the given criteria
* Again using `contains()`, _but_ **note** that here we're renaming `Mass` with `Ore.Mass = Mass` and `Appraisal` with `Ore.Value = Appraisal`
  > The `rename()` function keeps all of the columns and allows you to rename individual columns

## Filtering

Filtering allows us to select rows based on given criteria

* Selecting all DIAMOND minerals that have PERIDOT in either of the minor mineral columns
  * Note the use of the `|` to indicate `or`
* Finding all minerals that have a combination of GEODES and ICE
  * Note the use of `|` for `or` and `&` for the use of `and`
  * Also not the use of `()` to set precedence in the logical operation
* Finding all minerals that have DIAMOND, SILVER, or PLATINUM in them
  * In this case we use the `%in%` operator in combination with a vector to filter on multiple criteria
