# Review Histogram Activity (0:10)

* Note: This file is to guide instructors in review the [Extra-Stu_Histogram](../../Unsolved/Extra-Stu_Histogram) activity.

* Open up the solved [plots.js](./plots.js).

* Remind students that a `trace` is an object describing the points to draw, and how to draw them.

  * Explain the meaning of the `x` and `type` properties of `trace`.

  ![histogram trace](../../../Images/histogram1.png)

* Remind students that, to create plots, Plotly expects an _array of trace objects_, traditionally called `data`.

  * Point out that, in this case, we only have _one_ trace to plot, so `data` will be an array containing the single object.

* Remind students that `layout` is an object that configures the presentation of the plot.

  * Explain the meaning of the `bargap` property.

  ![histogram bar gap](../../../Images/histogram2.png)
* Point out that the bonus, while challenging, illustrates a number of fundamental concepts.

* Open the solved [bonus.js](./bonus.js).

* Explain that, after ensuring we can get a basic plot to display, we should enhance our visualization by:

  * Cleaning up our data, and

  * Tightening up the constraints on the plot (e.g., getting things to fit better, etc.)

* Explain that a common first step in cleaning up data for plots is throwing out outliers.

* Explain that a common technique for this is to:

  * Calculate the data set's **i**nter**q**uartile **r**ange (IQR)

  * Use the IQR to define boundaries/"thresholds" about the upper and lower quartiles

  * Use these thresholds to `filter` the original data set

* Explain how the above logic is implemented in the solution.

* Emphasize the following:

  * Why we must `sort` the input array to calculate percentiles/quartiles

  * That defining a `maxValue` and `minValue` is akin to opening a "window" over the data set, retaining only data that falls within the opening

  * The use of `filter`

  ![filtered outliers](../../../Images/histogram3.png)

* Optionally, discuss:

  * The motivation for using `concat` to copy the input array

    * Explain that `sort` updates its antecedent in-place.

    * Explain that copying the array, and sorting the copy, minimizes side effects.

    * Explain that operating on copies of input data, rather than the original data, is a general best practice.

* Point out that we use `filteredOutliers` to process `speedOfLight`, and that we calculate the `min` and `max` of the data set.

  ![filtered](../../../Images/histogram4.png)

* Explain that we can use the data set's minimum and maximum values to set "intelligent" bounds on the plot.

  * Emphasize scaling axes with respect to the underlying data is a general best practice.

  ![scaling](../../../Images/histogram5.png)
