# Grouping Data to Summarise

> From here down I will give a brief description of the pertainent points for each block within the markdown starting after reading in the tibble. **One _top-level_ bullet point per code block**
>
> * Adding new columns through the `mutate` functon
>   * Pay special attention to how mutate can be used to create new columns identically to creating a new tibble colun-wise
>   * The mutate assigns the data to a new `tibble`, a `select` pipe is used to boil up and print the new columns
> * Ranking the value density of all minerals using `group_by`
>   * A `mutate` function is used to create the `Value.Position.Overall` with the help of `min_rank` which creates a rank for each row based on the input column; in this case `Value.Density`
>   * A `group_by` is used on the `Major.Min.Comp` column
>   * A `mutate` is used again to create another column, again using `min_rank`.
>     * This time the use of `min_rank` creates a ranking within the groups
>   * To observe the before and after difference, a pipeline has been created below the operation
>     * First the columns of interest are brought to the front through a `select` statement
>     * The `arrange` statement is demonstrated here
>       * This is `dplyr`'s fancy function for sorting
>       * The `desc` function tells `arrange` to sort by descending
>       * _**This could be left out if you think it's superfluous**_
>     * Finally `filter` is used on `Value.Position.by.Major` to demonstrate that there are mutiple rank 1' for this column. 
>     * Feel free to drive home the point by commenting out the previous filteration step and uncomment instead 
>       `filter(Value.Position.Overall==1)`
>       * Doing this will give only a single row back
> * The `summerise` function
>   * A new tibble is returned with a single row.
>     * The column names are decided by the user
>     * `Mass.CoV`- CoV stands for Coefficent of Variation
>       * This is a normalized measure of the variabiliy of a set of data
>       * Can overstate (with very small numbers) or understate (with very large numbers) the variability within a set of data points
>       * Should be taken within the context of the real numbers used to calculate the CoV.
> * Grouping then summerising
>   * When first grouping then summarising, a single row per group is created with a summary for each group.
>   * This should feel similar to `panadas`
> * Mutiple groupings
>   * A single row per grouping is again created and the summary per grouping s given
>   * This is similar to the last example and should again feel very similar to working within `pandas`
