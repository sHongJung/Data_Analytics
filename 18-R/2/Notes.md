### Goals

* First half: Learn more R
* Second half: Work on projects

### Notes

* Make sure to send us project proposals by the end of the day today. M/W class send to me, T/Th class: do whatever Matt told you :)

### Exercises

#### Instructor Demo on the pipe operator (5 min)

* The pipe operator passes the output of the expression on the left of the pipe operator to the function on the right of it. On the right, you typically have a function, since you need to do something with the input you're receiving!
* When you start storing the results of one function in intermediate variables you pass to other functions, or when you start wrapping functions with many other functions (e.g. `func1(func2(func3(val)))`), it gets hard to understand what's going on. The pipe operator can make these kind of statements easier to read.
* [More on the pipe operator](http://r4ds.had.co.nz/pipes.html)
* RStudio provides a [keyboard shortcut](https://support.rstudio.com/hc/en-us/community/posts/201879243-keyboard-short-cut-for-) for the pipe operator

#### Instructor Do Exercise 1 - UFO Sightings (10 min)

* Here, we use the pipe operator a lot to help y'all build an intuition for how it works
* `ufo %>% count()` counts the number of records in the UFO tibble.
* `ufo$state %>% unique() %>% length()` counts the number of unique states in the dataset
* The `groupby %>% summarise %>% arrange` pattern is conceptually similar to what we did in `pandas` a long time back.
* **We can already see how the pipe operator reduces the code to its essence**
* `groupby(col)` groups our tibble by the given column
* `summarise(name = exp)` creates a new column `name` on our grouping with the value set to the expression `exp`
* You can pass multiple `name = exp` pairs, separated by commas, e.g. `summarise(avg.duration = mean(`duration (seconds)`), num.sightings = n())`
* `arrange(col1, col2, ...)` sorts by the columns passed to it, ascending by default. You can use `arrange(desc(col1))` to sort by `col1` in descending order.

#### Instructor Do Exercise 2 - Creating our own Tibbles (10 min)

* Remember that "tibbles" are part of the `tidyverse` package, so we must run `library(tidyverse)` or `require(tidyverse)` before creating tibbles.
* tibbles can be created by column or by row (much like DataFrame objects in `pandas`), and the `tidyverse` provides two corresponding functions for creating tibbles as a result.
* When creating DataFrames, we can create columns that are based on the values of other columns, *even before we create the DataFrame*. For instance, given a `Population` and a `Square.Miles` column, we can create a `Population.Density` column by passing this in in the list of name = vector pairs to the `tibble` function: `Population.Density = Population/Square.Miles`.
* `tibble(Col1=c(1, 2, 3), Col2=(4, 5, 6))` creates a tibble of two columns, `Col1` and `Col2`, each with the corresponding vector of data passed to them.
* `frame_data()` accepts columns, preceded by `~`, followed by the data associated with those columns. This can get hard to read if you're passing in all of this data manually. 
* In your day-to-day, you may encounter data delimited by tabs instead of commas. `read_tsv(file)` reads in a TSV (tab-separated-values) of data and returns a tibble.

#### Students Do Exercise 3 - Tibbles and Tibbles (15 min + 5 min review)

#### Instructor Do - Apply (10 min)

* In other languages we've seen, it's very common for us to apply functions to every element of a list, on an element-by-element basis.
* Examples: `for` loops or `map` in Python. `for`, `forEach` and `map` in JavaScript.
* We can use a `for` loop in R to iterate through every element of an existing vector or list and apply a function within the `for` loop. But if we simply want to apply a funciton on every element of an array-like object, we know it's probably simpler. In Python and JS, again, we had `map`.
* `sapply(vector, function)` will apply the given function to each element in `vector`, returning a new vector.
* `lapply` works the same, but returns a list instead of a vector.
* **When would I want to use a list vs. a vector? Vectors are homogeneous: they contain elements of the same type. Lists are heterogeneous: they can contain elements of different types.**

#### Students Do - School Tibble (20 min + 5 min review)
