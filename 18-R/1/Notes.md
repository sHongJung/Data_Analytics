### Goals

* Get a small introduction to R
* Intall RStudio, an IDE (integrated development environment) for R
* Establish groups, start project proposals

### A little bit about R + a small history

* R is a programming language used for data analysis, statistics, modeling and more.
* VERY big in the statistical and scientific communities. Since many scientists move into data science, R has spread into tech.
* Professional data scientists often work either in R, or Python, or both. R and Python are both full of most of the features data scientists need day-to-day.
* R has better statistical modeling support out of the box (built in functions for creating statistical simulations and models).
* The S language was developed around 1975 at Bell Laboratories, which is famous for other inventions it produced (the UNIX operating system, on which Linux and macOS are both based), and the transistor.
* R is an open-source implementation of S, and serves as the de-facto language for writing statistical software.
* I mention S because you may find older (still good) resources that mention S. Most S code will run in R.
* R has become quite a bit more popular in the past ~5 years. See [this amazing analysis](https://stackoverflow.blog/2017/10/10/impressive-growth-r/) by the Stack Overflow team.

### R resources

* [IF YOU READ ANYTHING, READ R for Data Science](http://r4ds.had.co.nz/)
* [R Basics Cheatsheet](https://www.rstudio.com/wp-content/uploads/2016/10/r-cheat-sheet-3.pdf)
* [A huge list of cheatsheets in R](https://www.rstudio.com/resources/cheatsheets/)
* [The Tidyverse - R Packages for Data Science](https://www.tidyverse.org/)
* [Learn all about the Tidyverse and related R tutorials](https://www.tidyverse.org/learn/)
* [Intro to Data Visualization with ggplot](http://r4ds.had.co.nz/data-visualisation.html)
* [RStudio Keyboard Shortcuts](https://support.rstudio.com/hc/en-us/articles/200711853-Keyboard-Shortcuts)

### Exercises

#### Exercise 0 - Everyone Do Install RStudio, `require` and `install.package`

* [Download RStudio here](https://www.rstudio.com/products/rstudio/download/#download).
* Open up the `prework.R` file in RStudio. You should see the contents of this file load in the top pane (the "source" code). You can run this code by selecting the lines you want to run and click the "Run" button.
* Keyboard shortcuts: you can run the line your cursor is currently on using `Cmd + Enter` on a Mac or `Ctrl + Enter` on a PC. You can run _all_ the code in the source pane using `Cmd + Shift + Enter` (from now on, I'll write down the Mac keyboard shortcuts. If you're on a PC, you'll typically replace `Cmd` with `Ctrl`). 
* Access all keyboard shortcuts by going to `Help -> Keyboard Shortcuts Help`.
* `require("packageName")` loads a package into the current namespace, which just makes it available for use in your R program. This is logically equivalent to `import` in Python. You may also see `libary("packageName")` used, which is functionally the same.
* The first time we try to run `require("tidyverse")`, we get an error. The `tidyverse` library isn't installed! We have to use `install.packages("tidyverse")` to install it.
* After installation, run `require("tidyverse")` again. Note that you may encounter "Conflicts" when you run this. This means that `tidyverse` includes some functions that have the same name as functions loaded into the current namespace (functions built-into R's base packages). In this particular case, this is fine. [This Github issue](https://github.com/STAT545-UBC/Discussion/issues/331) explains this in more depth.

### Exercise 1 - Basic R syntax (15 min)

* `<-` is our assignment operator. `a <- 3` initializes the variable `a` with the value `3`.
* Small note: `=` also works for assignment, and there's no functional difference between `=` and `<-`. `<-` is more conventional in R and most people use that. See [this blog post](http://blog.revolutionanalytics.com/2008/12/use-equals-or-arrow-for-assignment.html) for more info.
* In R, vectors allow us to store items of the same type. In Python, remember that we could store items of different types.
* You can create a vector using `c(item 1, item 2, ..., item n)`, e.g. `v <- c('a', 'b')`. `c` stands for "combine".
* If you try to store items of a different type in the same vector, R will "coerce" the items to the same type.
* Very important: **Vectors are indexed starting at 1, instead of 0, like in most other languages we've used**. 
* A for loop in R is similar to loops in other languages:

    ```
    vec <- c(1, 2, 3)
    for (x in vec) {
      print(x)
    }
    ```

* You can apply operations on vectors in more complex ways:

    ```
    combined_vector <- c(1, 2, 3, 4)
    numeric_vector <- 1:length(combined_vector)   # Returns (1, 2, 3, 4)
    squared_vector <- numeric_vector**2   # Returns a vector of elements in numeric_vector that are all squared
    ```

* An `if` statement is also similar to what we've seen in other languages:

    ```
    for (prez in presidents){
        if (nchar(prez) > 5){
            next
        }
        else {
          print(prez)
        }
    }
    ```

* A list in R is a bit like a Python dictionary (it's weird, I know).
* Use `names(list)` to get the names / keys (R calls these "tags") of the list.
* Access a single given tag / value pair with `list["tag"]`.
* Access the _values_ of a given tag with `list[["tag"]]`. **Note the double brackets here, vs. the single brackets above**.
* Functions can be created similar to how we'd do in JavaScript. `function(args) { }` begins our function declaration, with the relevant code within the brackets. We `return` whatever we want at the end of the function. Finally, we assign the function to a name using the assignment operator.
* The `typeof` command gives you the type of the variable (including vectors).

#### Exercise 2 - Students Do We R in Junior High Again (15 min + 5 min review)

#### Exercise 3 - Instructor Do Vectors (10 min)

* We can assign `names` to vectors in R, just as in Python, we can assign indexes to a Series. Just as an array can be used to index a Series in pandas, a vector in R can be paired up as names for another vector.
* `names(precipitation) <- months`
* After this, we can access the tag / value pair using `precipitation["Mar"]`. We can access only the value using `precipitation[["Mar"]]`
* `summary(precipitation)` returns summary statistics on the precipitation data in our vector.
* `sd(vector)` returns the standard deviation of the data in a numeric vector.
* `length(vector)` returns a vector's length.
* `sum(vector)` returns the sum of the elements of a numeric vector.

#### Exercise 4 - Instructor Do File Structure Navigation (10 min)

* `getwd()` returns the current working directory: think of this like you've run `cd` into that directory. All references to files and directories are relative to this directory.
* `dir()` returns a vector of the files and directories in the current working directory.
* `setwd(dir)` sets the current working directory to `dir`.
* If we've run `require("tidyverse")` before we load our CSV, we'll use the `read_csv` function used by the `tidyverse`, which returns a datatype called a "tibble".
* We can load a CSV using `read_csv`, e.g. `t <- read_csv('data.csv')`. We want to assign the return value of `read_csv` to a variable so we can reference the data later.
* `head(data)` prints the first few lines of our tibble, just like `df.head()` in pandas.

#### Partners Load CSVs, talk about R syntax (7 min + 5 min review)

* **Make sure you can load the `data.csv` file from the previous exercise**.
* Talk with a partner about the similarities and differences between the syntax for assignment, creating function, etc. in R, Python, and JavaScript.
* We'll briefly talk about this as a class.

#### Exercise 5 - Instructor Do Reading CSVs, Working with Tibbles and DataFrames (10 min)

* We can load a tibble that comes with a specific package in R using `data(diamonds, package='ggplot2')` (get the `diamonds` tibble from the `ggplot2` package).
* *A tibble is just a dataframe*. A dataframe is a lot like the DataFrame object we're used to in `pandas`.
* Tibbles improve on the `data.frame` object in a couple of ways: 1.) printing tibbles only print the first 10 rows of the object (vs. hundreds of rows for larger data sets). 2.) subsetting tibbles (extracting specific columns of data) works more like we'd expect. Subsetting normal dataframes allows partial column name matching (e.g. `df$a` will return a column that just starts with "a", where a tibble of the same data will require you to provide the exact column name. This can help reduce errors. See [this reference](http://r4ds.had.co.nz/introduction-2.html) for more information on tibbles.
* We'll review a few of the functions from a library called `dplyr`, which we import when we load the "tidyverse" package. Behind the scenes, R loads a number of packages when we load the tidverse.
* [Chapter 5 of R for Data Science](http://r4ds.had.co.nz/transform.html) covers each of these functions in much more detail.
* The conceptual workflow should feel a lot like working in `pandas`.

#### Exercise 6 - Students Do Back to School (20 min + 10 min review)

### The tidyverse

* [The tidyverse](http://tidyverse.tidyverse.org/) is a collection of R packages that handle common data manipulation and visualization tasks with ease. These packages facilitate data science with R and have completely changed the game.
* These packages were all created by [Hadley Wickham](http://hadley.nz/), a statistician. He is the most famous R programmer around. 
* We'll use a handful of the packages here today.
* When you run `require("tidyverse")`, you're actually loading a number of libraries (`dplyr`, `ggplot2`, etc.) behind the scenes. Given how R loads functions into the namespace, you don't have to specify the package name, like `dplyr.function_x` or `ggplot2.function_y`. You just run the function and it works. This makes these functions feel like a core part of the language.
