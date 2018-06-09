# Introduction to Tibbles

* Call for the `tidyverse` library
  * Emphasize that we're going to use the tidyverse throughout today
  * The `tidyverse` is a collection of other libraries that make up a set of reccommened workflows.
  * There are other ways to do all of what the `tidyverse` does.
  * For convience append \*.tb to the end of the variable names for the tibbles. This is \_not_required.
* Compare the manual creation of a `tibble` to the creation of a `dataframe` in Python
  ## Creation Column-wise
* Uses the `tibble()` function from the `tidyverse`
* Contrast by pointing out the ability to immeaditly operate on data in the the middle of creating the `tibble`.
  ![Operating on data before tibble creation][opdatatbcreate]
  ## Creation Row-wise
* Uses the `frame_data()` function from the `tidyverse`
* Columns are denoted by `~`
  * In this case the `~` is a way to indicate column names without having to quote them. 
    * This is provided by the `lazyeval` library loaded with the `tidyverse`.
  * In most other cases the `~` stands for **depends on** and is used in  in formulas.
    ## Read in a file
* The `readr` library loaded with the `tidyverse` allow us to read all kinds of file formats
* Have the students do `?read_csv` to see what is included (they  need to have loaded the `tidyverse`).
* Note: `read_csv()` and `read_tsv()` are convinience functions that are really `read_delim` with assumptions made for you. Use `read_delim` if the file is text readable but you have a special case for how it's formatted

[opdatatbcreate]: ../../../../Images/TibbleCreatAndOperate.png
