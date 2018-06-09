### Instructor Do: Pipelines and the >%> Operator (0:15)

* **Instructor Note**: [Objectives.md](Activities/Solved/01-Ins_Piping/Objectives.md)

- - -

* Point out that a lot of data analysis requires us to perform a _sequence_ of transformations to our data.

  * For example, we might load financial data for our department; _then_
  * Extract only columns containing employee salary information; _then_
  * Scale that column to use units of "hundreds of thousands" of dollars; _then_
  * Calculate total payroll; and _finally_,
  * Format the output for printing.

* Explain that this process is so common in data analysis that R and the tidyverse provide special utilities for writing such transformation sequences.

* Explain that this demonstration will introduces students to:

  * Function pipelines in general.

  * The use of the `%>%` to define pipelines.

* Open the slide in [Slides/Piping_in_R.pptx](Slides/Piping_in_R.pptx)

* Take a moment to explain the Python code

  ![Images/pipe1.png](Images/pipe1.png)

* Explain that to perform a multi-step calculation, we have traditionally:

  * Assigned a computation to a variable,
  * Passed off the results to a subsequent calculation,
  * Assign its results to another variable

* Instead of creating a new variable in each intermediate step, what if we could pass off the results of one step to the next step •while\* increasing legibility?

* Open the demonstration in [Activities/Solved/01-Ins_Piping/piping.rmd](Activities/Solved/01-Ins_Piping/piping.rmd).

* Each chunk in the R Markdown is followed by its equivalent that uses piping. Demonstrate each one.

* For example, `head(diamonds)`, where `diamonds` is the name of the data set, can use piping thus:

  ```r
  diamonds %>% head()
  ```

* Explain that the `%>%` means: "Take what's to the left, and pass it as the _first_ argument to the function on the right.

  * The keyboard shortcut for this symbol is `Cmd+Shift+M` in Macs and `Ctrl+Shift+M` in Windows.

* Point out that this syntax makes the transformations more readable.

* Point out that piping becomes especially useful as we increase the number of operations:

  ```r
  diamonds %>%
      group_by(cut) %>%
      summarize(mean(price), sum(price))
  ```

* Contrast the above with nested code that accomplishes the same thing:

  ```r
  summarize(group_by(diamonds, cut), mean(price), sum(price))
  ```

  * Piping makes this series of operations much more intuitive for the programmer, and much more readable for everyone else.

* Take a moment to address remaining questions before proceeding.

### Students Do: Pipe Dreams (0:15)

* Instructions for this activity are provided as comments in the provided file.

* **Files**:

  * [Piping_Vectors.rmd](Activities/Unsolved/02-Stu_Piping/Piping_Vectors.rmd)

### Everyone Do: Review Activity (0:05)

* Remind students that the objective for this exercise is to use the pipe operator to express pipelines, sequences of function applications.

* Open the solved [Piping_Vectors.Rmd](Activities/Solved/02-Stu_Piping/Piping_Vectors.Rmd).


* Take a moment to address remaining questions before proceeding.

### Students Do: Tibbles and Tibbles (0:10)

* **Files**

  * [other_franchise.tsv](Activities/Unsolved/04-Stu_Troublesome_Tibbles)

* **Instructions**

  * [README.md](Activities/Unsolved/04-Stu_Troublesome_Tibbles/README.md)

### Everyone Do: Review Tibbles (0:05)

* Remind students that this activity was meant to provide practice creating tibbles in three ways:

  * In column-wise fashion, with `tibble`

  * In row-wise fashion with `frame_data`

  * From a file, with  `read_tsv` or `read.table`.

* Open the solved [Stu_Troublesome_Tibbles.R](Activities/Solved/04-Stu_Troublesome_Tibbles/Stu_Troublesome_Tibbles.R).

* Explain that, to create the `cute.tb` tibble, we pass a series of named vectors.

* Explain that the first column is named `Deck`, and contains the values passed to the vector constructor.

* Explain that `Starting.Tibbles` contains the numbers `5` through `9`, inclusive.

  * Point out that we use the [colon operator](https://stat.ethz.ch/R-manual/R-devel/library/base/html/Colon.html) to generate the sequence of integers: `5, 6, 7, 8, 9`.

  * Point out that manually passing these values individually would work, but that the colon operator is more idiomatic.

* Finally, point out that we derive `Current.Tibbles` by multiplying the `Starting.Tibbles` column.

```r
cute.tb <-
  tibble(
    Deck = c("Engineering",
             "Mess Hall",
             "Brig",
             "Bridge",
             "Nacelle Maintence Tunnels"),
    Starting.Tibbles = 5:9,
    Current.Tibbles = (2^10)*Starting.Tibbles
)
```

* Ask a student to explain how to create the `crew.tb` tibble.

* Explain that, to create `crew.tb`, we:

  * Pass a list of column names, prepending each name with a tilde (`~`)

  * Pass data in _row-wise_ fashion.

```r
crew.tb <- frame_data(
  ~Name, ~Final.Rank, ~Years.of.Service,
  "Kirk", "Captain", 39,
  "Spock", "Captain", 115,
  "Mathews", "Crewman", 1,
  "Rayburn", "Crewman", 3,
  "O'Herlihy", "Ensign", 2,
  "Lang", "Lieutenant Commander", 7
)
```

* Finally, explain that, to load data from `other_franchise.tsv`, we use `read.table`.

  * Point out that `read_tsv` achieves the same effect.

* Take a moment to address remaining questions before proceeding.

### Instructor Do: Extracting Data from Tibbles (0:15)

* **Instructor Note**: [Objectives.md](Activities/Solved/05-Ins_Piping_Filters)

- - -

* Point out that we'll often load tibbles with more data than we need to solve a given problem.

  * For example, if we need to calculate total payroll for a given department, all we need are employee salaries, and a range of dates over which to calculate payroll.

* However, we'll often find that the only data we have access to includes _every_ piece of financial data the department has _ever_ collected.

* Explain that, in these cases, R provides tools for extracting just the data we need.

* Explain that the next notebook will demonstrate how to:

  * Preview the contents of a tibble with `head` and `tail`

  * Extract specific columns, with `select`

  * Filter out rows that match a specific criterion, with `filter`

* Open [Ins_Filtering.rmd](Activities/Solved/05-Ins_Piping_Filters/Ins_Filtering.rmd).

* Point out that we begin by reading data from `Minerals.csv`. We'll refer to this data for the rest of the demonstration.

```r
minerals.tb <- read_csv("Minerals.csv")
```

#### Previewing with head and tail

* Explain that R provides two functions, `head` and `tail`, which allow us to preview the first or last elements of a tibble, respectively.

  * Explain that we can pass a number to either `head` or `tail`, which will limit the number of rows output by the function.

* Explain that we can also pipe tibbles to `print`, and specify how many rows we'd like to view.

```r
minerals.tb %>%
  head()

minerals.tb %>%
  tail(5)

minerals.tb %>%
  print(n=100)
```

#### Extracting data with `select`

* Point out that, when we want to extract data from data frames, we'll often want to extract _columns_ of data.

* Explain that `select` allows us to extract columns by name.

* Explain that the snippet below creates a new tibble containing _only_ the `Major.Min.Comp` and `Appraisal` columns from `minerals.tb`.

```r
# Select by column name
minerals.tb %>%
  select(Major.Min.Comp, Appraisal)
```

* Explain that `select` also allows us to _omit_ columns by name.

* Explain that adding a `-` in front of a column name extracts everything _except_ for that column.

  * Explain that the snippet below creates a new tibble which contains every column in `minerals.tb`, _except_ for `Mass`.

```r
# Omit by column name
minerals.tb %>%
  select(-Mass)
```

* Explain that `select` also allows us to extract and omit columns by index.

  * Explain that the snippets below extract the 1st, 2nd, 4th, and 5th columns from `minerals.tb`; and everything _except_ for the 1st and 2nd column, respectively.

```r
# Select by index
minerals.tb %>%
  select(1:2,4:5)

# Omit by index
minerals.tb %>%
  select(-(1:2))
```

* Finally, explain that we can exercise finer control over what `select` extracts or omits by using it in conjunction with `starts_with`, `ends_with`, and `contains`.

  * Explain that each of these functions is self-explanatory. They allow us to select only columns whose names _start with_, _end with_, or _contains_ a given string value, respectively.

* Explain that the snippet below extracts all columns that start with `"Major"`, _or_ end with `"Comp2"`.

  * Explain that, for the `minerals.tb` tibble, this extracts the `Major.Min.Comp` and `Minor.Min.Comp2` columns.

![](Images/starts_ends_with.png)

* Explain that adding a `-` in front of any of these helpers _omits_ columns.

```r
# Omit columns containing the word `Minor`
minerals.tb %>%
  select(-contains("Minor"))
```

#### Changing column names with `rename`

* Explain that we can rename columns when using `select` by simply mapping old column names to new ones.

* Explain that the snippet below creates a new tibble containing every column containing the string `"Min"`, but renames `Ore.Mass` to `Mass`, and `Ore.Value` to `Appraisal`.

```r
minerals.tb %>%
    select(contains("Min"), Ore.Mass = Mass, Ore.Value = Appraisal)
```

* Explain that we can achieve the same thing _after_ creating a tibble by calling `rename`.

```r
minerals.tb %>%
  rename(Ore.Value = Appraisal)
```

#### Extracting data with `filter`

* Finally, explain that we can use `filter` to extract rows based on boolean tests.

* Explain that, in the snippet below, we

  * First, `select` `Appraisal`; columns containing the string `"Min"`; and rename `Ore.Mass` to `Mass`. We save the new tibble to `less.min.tb`.

  * Then, we extract only the rows whose `Major.Min.Comp` value is equal to `"DIAMOND"`. We then save this to `less.min.tb`.

  * Finally, we further extract only rows whose `Minor.Min.Compl` _or_ `Minor.Min.Comp2` value is equal to `"PERIDOT"`.

    * Emphasize the use of the pipe character (`|`) to indicate logical or.

```r
less.min.tb <- select(minerals.tb, contains("Min"), Ore.Mass = Mass, Appraisal)
less.min.tb <- filter(less.min.tb, Major.Min.Comp == "DIAMOND")
less.min.tb <- filter(less.min.tb, (Minor.Min.Comp1 == "PERIDOT") | (Minor.Min.Comp2 == "PERIDOT"))
```

* Ask a student to remind you of the last time they saw such a series of assignments and function calls.

  * Remind students that the last time we saw this pattern was when studying pipes.

* Remind students that we can rewrite such expressions as a sequence of nested function calls.

```r
# Run as one long nested set of functions
filter(filter(select(minerals.tb, contains("Min"), Ore.Mass = Mass, Appraisal), Major.Min.Comp == "DIAMOND"),
       (Minor.Min.Comp1 == "PERIDOT") | (Minor.Min.Comp2 == "PERIDOT"))
```

* Nesting function calls is better style, but this syntax is unreadable.

* Remind students that they can use pipes to rewrite such nested function calls.

  * Point out that the structure of the snippet below makes the structure of the transformations more obvious, and the code, more readable.

```r
minerals.tb %>%
  select(contains("Min"), Ore.Mass = Mass, Appraisal) %>%
  filter(Major.Min.Comp == "DIAMOND") %>%
  filter((Minor.Min.Comp1 == "PERIDOT") | (Minor.Min.Comp2 == "PERIDOT"))
```

* Take a moment to address remaining questions before proceeding.

### Students Do: Filtering & Piping (0:15)

* **Files**

  * [Stu_Select_Filtering.rmd](Activities/Unsolved/06-Stu_Filter_Piping/Stu_Select_Filtering.rmd)

* **Instructions**

  * [README.md](Activities/Unsolved/06-Stu_Filter_Piping/README.md)

### Everyone Do: Review Filtering & Piping (0:05)

* Remind students that the objectives of this activity are to practice:

  * Using `select` to extract specific columns of a tibble

  * Using `filter` to extract specific rows of a tibble

  * Using `starts_with`, `ends_with`, and `contains` to specify groups of columns to extract

REVIEW

* Open the solved [Stu_Select_Filtering.rmd](Activities/Solved/06-Stu_Filter_Piping/Stu_Select_Filtering.rmd) notebook.

* Point out that we begin by using `read_csv` to load data from `cereals.csv`.

```r
cereal.tb <- read_csv("./cereals.csv")
```

* Ask a student to explain how to extract every column in `cereal.tb`, _except_ for `rating` and any column ending in -_ium_.

  * Explain that we use `select`, along with the `-` operator, to omit columns.

```r
cereal2.tb <- cereal.tb %>%
  select(-rating, -contains("ium"))
```

* Ask a student to explain how to filter out rows whose `type` is equal to `"H"`.

  * Explain that we use `filter`, and pass a test directly.

```r
cereal2.tb %>%
  filter(type=="H")
```

* Ask a student to explain how to filter rows whose `mfr` value is equal to `"A"`, `"N"`, `"Q"`, or `"R"`.

  * Explain that the "obvious" way to achieve this is to use `filter` with the pipe operator.

```r
cereal2.tb %>%
  filter(mfr == "A" | mfr == "N" | mfr == "Q" | mfr == "R"))
```

* Point out that, while this works, it's repetitive.

  * Explain that we can use an `%in%` clause to accomplish the same behavior more idiomatically.

```r
cereal2.tb %>%
  filter(mfr %in% c("A", "N", "Q", "R"))
```

* Ask a student to explain how to extract rows with calorie counts below 100 _and_ fiber counts greater than or equal to 3.

  * Explain that we use `filter` in conjunction with the `&` operator.

```r
cereal2.tb %>%
  filter(calories < 100 & fiber >= 3)
```

* Ask a student to explain how to extract rows with sugar counts greater than 11 _or_ fat counts greater than 3.

  * Explain that we use `filter` in conjunction with the `|` operator.

```r
cereal2.tb %>%
  filter(sugars > 11 | fat > 3)
```

* Take a moment to address remaining questions before proceeding.

### Instructor Do: Grouping & Summarise (0:10)

* **Instructor Note**: [Objectives.md](Activities/Solved/07-Ins_Grouping_Summarise/Objectives.md)

- - -

* Point out that we'll often want to modify the data within our tibbles.

* Explain that we may need to divide every value in a column by a given factor.

* Also point out that, often, we need to create groups out of rows which share the same values in a given column.

  * For example, we might group people in a classroom by their birth month.

* Explain that the objectives for this lesson are to:

  * Use [mutate](https://www.rdocumentation.org/packages/dplyr/versions/0.5.0/topics/mutate) to update and add columns to a tibble.

  * Use [group_by](https://www.rdocumentation.org/packages/dplyr/versions/0.7.3/topics/group_by) to condense tibbles.

  * Use [summarise](https://www.rdocumentation.org/packages/dplyr/versions/0.7.3/topics/summarise) to reduce multiple values into one.

* Open [Ins_Grouping_Summarise.rmd](Activities/Solved/07-Ins_Grouping_Summarise/Ins_Grouping_Summarise.rmd).

* Point out that, to start, we load the data in [minerals.csv](Activities/Solved/07-Ins_Grouping_Summarise/minerals.csv).

```r
minerals.tb <- read_csv("minerals.csv")
```

#### Mutate

* Explain that, to add or update columns, we use a function called `mutate`.

* Explain that `mutate` accepts a tibble, as well as a map of column names to their new values.

  * Explain that `mutate` is often used to create _derived_ columns.

* Scroll to the snippet below in the notebook.

  * Explain that, in the snippet below, we divide every figure in the `Mass` column by 2; create a `Value.Density` column, equal to the quotient of `Appraisal` and `Mass`; and add `Log10.Value.Density`, which is the log10 of the `Value.Density` column.

```r
minerals2.tb <- minerals.tb %>% mutate(
  Mass = Mass/2,
  Value.Density = Appraisal/Mass,
  Log10.Value.Density = log10(Value.Density)
)
```

* Explain that the code in the snippet below creates a tibble with the columnes `Value.Density` and `Log10.Value.Density` as the _first_ two columns, with everything else following.

```r
minerals2.tb %>%
  select(Value.Density, Log10.Value.Density, everything())
```

#### Groupby

* Scroll to the below excerpt, and explain the following points.

```r
ranked.minerals <- minerals2.tb %>%
  mutate(Value.Position.Overall = min_rank(desc(Value.Density))) %>%
  group_by(Major.Min.Comp) %>%
  mutate(Value.Position.by.Major=min_rank(desc(Value.Density)))
```

* Explain that `group_by` accepts a tibble and a column name, and creates groups of rows that contain the same value within the given column.

* Point out that, since `mutate` returns a tibble, its output can be piped to `group_by`.

* Explain that the snippet below first adds a `Value.Position.Overall` column; then creates groups out of rows that share a `Major.Min.Comp` value; and, finally, adds a `Value.Position.by.Major` column.

* Explain that `min_rank` accepts a column name, and creates a new column which contains the _rank_ of each row in the original column.

  * E.g., it labels the row with the fifth largest entry for the column with `5`; the row with the 100th largest entry with `100`; etc.

  * Note the use of `desc` to reverse the ranking order.

* Scroll to the snippet below, and ask a student to explain it.

  * Explain that this snippet first reorders the columns with the `select` clause; then, arranges the rows of the tibble in descending order of `Value.Density`; and, finally, filters out only rows with a `Value.Position.by.Major` value equal to `1`.

```r
ranked.minerals %>%
  select(Value.Position.by.Major, Value.Position.Overall, Value.Density, everything()) %>%
  arrange(desc(Value.Density)) %>%
  filter(Value.Position.by.Major==1)
```

#### Summarise

* Explain that, often, we'll want to reduce a tibble to a summary of the data within it.

* Explain that this is what the `summarise` function is for.

* Scroll to the snippet below.

* Explain that this code creates a _summary_ tibble, with `Mass.Sum`; `Mass.Mean`; etc., columns, each of which will contain a single value: `sum(Mass)`, `mean(Mass)`, etc. respectively.

```r
minerals.tb %>%
  summarise(Mass.Sum=sum(Mass),
            Mass.Mean=mean(Mass),
            Mass.SD=sd(Mass),
            Mass.Median=median(Mass),
            Mass.CoV=Mass.SD/Mass.Mean,
            Value.All=sum(Appraisal),
            Count=n())
```

* Explain that `summarise` can also be used with _grouped_ tibbles.

  * Point out that the snippet below is similar to the above, but this time, we pipe the output of a call to `group_by` to `summarise`, rather than passing the tibble directly.

```r
minerals.tb %>%
  filter(Major.Min.Comp %in% c("DIAMOND", "SILVER", "PLATINUM")) %>%
  group_by(Major.Min.Comp) %>%
  summarise(Mean.Mass=mean(Mass),
            Total.Mass=sum(Mass),
            Distinct.Minor.Mineral1=n_distinct(Minor.Min.Comp1),
            Distinct.Minor.Mineral2=n_distinct(Minor.Min.Comp2),
            Distinct.Minor.Mineral.All=n_distinct(c(Minor.Min.Comp1,Minor.Min.Comp2)),
            Sample.Count=n())
```

![Output from the above call.](Images/group_summary.png)

#### Multiple Groupings

* Finally, explain that we can pass multiple column names to `group_by`.

  * Remind students that, in this case, it wll create groups for rows that share values in each of the columns passed to `group_by`.

```r
minerals.tb %>%
  filter(Major.Min.Comp %in% c("NEPTUNITE", "KUNZITE", "GAYLUSSITE", "CUBANITE")) %>%
  group_by(Minor.Min.Comp1, Major.Min.Comp) %>%
  summarise(Sample.Count = n(),
            Total.Value = sum(Appraisal),
            Total.Mass = sum(Mass),
            Value.Density = Total.Value/Total.Mass)
```

![Output summary of tibble with multiple groupings.](Images/multiple_groupings.png)

* Take a moment to address remaining questions before proceeding.

### Students Do: DataStorms (0:20)

* **Files**

  * [Stu_DataStorms.rmd](Activities/Unsolved/08-Stu_DataStorms/Stu_DataStorms.rmd)

### Everyone Do: Review DataStorms (0:10)

* Remind students that the primary objectives of this activity were to use `group_by` and `summarise` to explore storm data.

* Open the solved [Stu_DataStorms.rmd](Activities/Solved/08-Stu_DataStorms/Stu_DataStorms.rmd) notebook.

* Ask a student to explain how they created a table of how many days per month had category 3+ storms before 1990.

* Explain that solving this requires us to filter out all years before 1990 with category 3+ storms; group by month; and then summarise.

```r
mystorms %>%
  filter(year < 1990, category >= 3) %>%
  group_by(month) %>%
  summarise(`Days.of.3+.Storms.Before.1990`=n()/4)
```

* Ask a student to explain how they found how many days per month had category 3+ storms during and after 1990.

  * Explain that we'll do the same thing as before, but filter for years _greater than or equal_ to 1990.

  * Point out that everything else will remain the same.

```r
mystorms %>%
  filter(year >= 1990, category >= 3) %>%
  group_by(month) %>%
  summarise(`Days.of.3+.Storms.After.1990`=n()/4)
```

* Ask a student to explain how they found the median pressure and range of pressures for each year.

* Explain that we must first group by year; then use `summarise`, setting `median_pressure = median(pressure)`, and `delta_pressure`—which represents the range—equal to `max(pressure) - min(pressure)`.

```r
mystorms %>%
  group_by(year) %>%
  summarise(median_pressure = median(pressure),
            delta_pressure = max(pressure) - min(pressure))
```

* Ask a student to explain how they found the mean and median pressures by year and name, for hurricanes only.

* Explain that we must first group by year and name; then, filter storms of status `"hurricane"`; and finally, use `summarise` to output the `mean(pressure)` and `median(pressure)`.

```r
mystorms %>%
  group_by(year,name) %>%
  filter(status == "hurricane") %>%
  summarise(mean.pressure = mean(pressure),
            median.pressure = median(pressure))
```

* Ask a student to explain how they found all unique storms by year and status.

* Explain that we first `group_by` `year` and `status`; then, use `summarise` to find distinct storm names within the groups.

```r
mystorms %>%
  group_by(year, status) %>%
  summarise(unique_storms = n_distinct(name))
```

* Finally, ask a student to explain how they calculated the average month in which category 4+ storms occurred each year.

  * Explain that we must first `group_by` year; then, filter all storms that were category 4 or higher; and finally, count distinct storms and calculate the mean month of occurrence.

```r
mystorms %>%
  group_by(year) %>%
  filter(category >= 4) %>%
  summarise(storm.count = n_distinct(name),
            mean_month = mean(month+day/month.to.days(month)+hour/24))
```

* Take a moment to address remaining questions before proceeding.

### Instructor Do: Plotly through R (0:10)

* **Instructor Note**: [Objectives.md](Activities/Solved/09-Ins_Soybeans/Objectives.md)

- - -

* Explain that visualization is one of R's greatest strengths.

* Remind students that they've already seen several ways to generate plots, including matplotlib; d3; and Plotly.

* Point out that Plotly has bindings to R, so students can leverage what they know of Plotly's APIs to create plots from R.

* Open the [Ins_Plotly_AgAiN.rmd](Activities/Solved/09-Ins_Soybeans/Ins_Plotly_AgAiN.rmd) notebook.

* Point out that the first thing we do is simply load the required libraries, and read in the data.

```r
library(tidyverse)
library(knitr)
library(plotly)

resistant.tb <- read_tsv("Herbicide_resistant_soybeans.tsv")
```

* Explain that we next use `gather` to collapse the `Year` and `Percent.GE.Soybean` columns to key-value pairs.

  * Explain that `-State` indicates that we do _not_ want to create key-value pairs out of the values in the `State` column.

```r
gathered.res.tb <- resistant.tb %>%
  gather(Year, Percent.GE.Soybean, -State)
```

* Point out that the columns of the output correspond to key-value pairs constructed by pairing each of the original year columns with each of the values in each of the rows.

![](Images/gathered_rows.png)

![](Images/gathered.png)

* Explain that gathering our data in this way create a tibble we can use directly with `plot_ly`.

```r
gathered.res.tb %>%
  plot_ly(x=~Year,
          y=~Percent.GE.Soybean,
          type='scatter',
          mode = 'lines+markers',
          color=~State,
          alpha=0.5,
          text=~paste("Year: ", Year, "<br>",
                      "Percent GE Soybean: ", Percent.GE.Soybean, "<br>",
                      "State: ", State))
```

* Point out that, while the syntax is different to that we learned when first diving into Plotly, the shape of the configuration is the same.

  * Emphasize that students can _already_ built complex plots with R by simply using Plotly.

![](Images/r_plotly.png)

* Take a moment to address remaining questions before proceeding.

### Students Do: GMO Cotton (0:10)

* **Files**

  * [ge_cotton.tsv](Activities/Unsolved/10-Stu_Cotton/ge_cotton.tsv)

  * [Stu_Plotly_Again.rmd](Activities/Unsolved/10-Stu_Cotton/Stu_Plotly_Again.rmd)

* **Instructions**

  * [README.md](Activities/Unsolved/10-Stu_Cotton/README.md)

### Everyone Do: Review Cotton (0:10)

* Remind students that the purpose of this activity was to practice using tibbles to create charts with Plotly.

* Open the solved [Stu_Plotly_Again.rmd](Activities/Solved/10-Stu_Cotton/Stu_Plotly_Again.rmd) notebook.

* Point out that we start, as always, by loading our data.

```r
cotton.tb <- read_tsv("ge_cotton.tsv")
```

* Ask a student to explain how they gathered their cotton data.

* Remind students that we want to plot GMO Cotton, by state, over time.

  * Explain that, to do this, we would gather on a key of `Year`, and a value of `Percent.GMO`.

  * Explain that we would omit `State` and `GMO Type` from gathering.

```r
gathered.cotton.tb <- cotton.tb %>%
  gather(key = Year,
         value = Percent.GMO,
         -c(State, `GMO Type`))
gathered.cotton.tb
```

* Ask a student to explain how they created tibbles for insect-resistant and herbicide-tolerant GMO cotton.

  * Explain that we would `filter` to extract only insect-resistant or herbicide-tolerance GMO cotton from `gathered.cotton.tb`.

```r
ins_resist <- gathered.cotton.tb %>%
  filter(`GMO Type`=="Insect-resistant (Bt) only")

herb_tol <- gathered.cotton.tb %>%
  filter(`GMO Type`=="Herbicide-tolerant only")
```

* Ask a student to explain how they configured their plots.

  * Point out that Plotly's configuration-based API is the same across platforms.

  * Explain that this allows us to simply configure Plotly with the same keys we'd use if working from JavaScript.

```r
ins_plot <- ins_resist %>%
  plot_ly(x=~Year,
          y=~Percent.GMO,
          type='scatter',
          mode = 'lines+markers',
          color=~State,
          alpha=0.5,
          legendgroup=~State,
          showlegend=F,
          text="Insect Resistant")

herb_plot <- herb_tol %>%
  plot_ly(x=~Year,
        y=~Percent.GMO,
        type='scatter',
        mode = 'lines+markers',
        color=~State,
        alpha=0.5,
        legendgroup=~State,
        text="Herbicide Resistant")
```

* Finally, ask a student to explain how they enabled subplots

  * Explain that the `subplot` function accepts the plots to arrange; how many rows to arrange them into; and whether or not to share axes.

```r
subplot(ins_plot,
        herb_plot,
        nrows=2,
        shareX = TRUE) %>%
  layout(title="GMO Cotton by State",
         margin = list(b=55))
```

* Take a moment to address remaining questions before dismissing class.
