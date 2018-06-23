## Goals

* Create groups and sets
* Create custom calculations (e.g. dividing one measure by another)
* Create maps
* If we have time, use Level Of Detail (LOD) calculations

## Notes

## Exercises

### Students Do Exercise 1 - Warm Up (15 min)

* [Reference on the Detail Marks property](https://onlinehelp.tableau.com/current/pro/desktop/en-us/viewparts_marks_markproperties.html#DetailProp)

### Everyone Review Exercise 1

### Instructor Do - Groups and Sets

* Note that we're using the [Text Mark](https://onlinehelp.tableau.com/current/pro/desktop/en-us/viewparts_marks_marktypes.html#TextMark) to display the sum of the profit for the given (state, ZIP) grouping. Just drag Profit into the "Label" mark and the sum of the profit should be displayed next to the grouping (given the dimensions in our Columns / Rows shelves).
* We're going to select multiple values / cells using Command + click or Control + click. On a Mac, for instance, hold Command and click one cell. **While still holding Command**, click on another. Both cells should be selected.
* Let's assume we wanted to group the profit for a handful of ZIP codes together. Maybe I'm the sales person for 3 particular zip codes and want to see the total profit across the 3. I can select the zip codes, right click, and choose to **Group** them. You can also use the paperclip icon that appears in the menu after selecting the items.
* Note that this creates a new field on the left.
* Moreover, we can go back to the original Data Source and create a group from the values of a particular field, allowing us to use that group as a dimension in any worksheet tied to this data source. Just click on the drop-down menu of any field (caret at the top right corner of the field) and click "Create Group". This also creates a completely new field with the grouping you've created.
* A set allows you to define a subset of data that meets the given conditions, and use that across your workbook. Conceptually, sets are like filters, but filters can only be applied to the current worksheet (unless you set a global filter on the data source level).
* Select the elements you want to include in a set, right click, and add them to a new set, naming the set. You'll see the set appear below the "Sets" header on the left. You can then use sets like any other dimension or filter, dragging the pill to the appropriate shelf.
* If we drag the set into the rows field and break data out by that set, we can see two distinct values tied to that set: "In" and "Out".
* We can also create sets based on more complex conditions. Right click on Sub-category and create a new set, click on the Condition tab and choose profit, including sub-categories with a profit of > $50,000.
* Move this set into the Filters shelf to include only Sub-categories with a profit of > $50,000
* Create a new set for "Low Shipping", adding a condition where the shipping cost is < $50,000.
* Then, right click on either set and choose the option to "Create combined set". Name the set, choose the other set you want to combine with this set, and select the option for "Shared members of both set" to include only members at the intersection of both sets.
* Like other dimensions, we can use this new set to identify items that are in or out of these sets by dragging the set into the Color mark.

### Students Do Exercise 3 - Dog Size and Intelligence (15 min)

### Everyone Review Exercise 3

### Instructor Do - Calculations

* We can define our own custom calculations based on the values of given measures or dimensions in our dataset, creating custom fields.
* To create a new Calculated Field, either right click anywhere in the Measures fields on the left of a Worksheet, or go to the **Analysis** menu and choose the option to "Create Calculated Field". Name the field **Profitability**, then use a conditional statement to create a custom formula tied to profit.
* The `IIF` function allows us to specify 1.) a condition, 2.) what value we should assign to the measure when the condition is true, 3.) what value to assign when that condition is false, and 4.) what value to return when the calculation return NULL or unknown.
* Like other languages we've seen, Tableau also has a `CASE` statement we can use here.
* See the [Logical Functions Reference](https://onlinehelp.tableau.com/current/pro/desktop/en-us/functions_functions_logical.html) for more information on these functions.
* We saw the **Number of Records** measure last class briefly. Think of this as equivalent to `COUNT(*)` in SQL: "I want to see the count of records given the groupings / breakout of dimensions applied". Move the **Number of Records** measure into the Text Mark icon and it'll add it to the table. Hover over each cell to see that number labeled as "Number of Records".
* The `COUNTD(field)` function is equivalent to `COUNT(DISTINCT(field))` in SQL: it'll return a count of the distinct values in field given the groupings applied.
* The "Calc diff" worksheet contains two bar charts: one on the top with sales broken out by category, and another on the bottom that shows the relative difference between one day's sales and another.
* To create this, move Sales into the rows shelf, click on the drop-down arrow on the measure, and choose "Difference" from the "Quick Table Calculation" menu.
* By default, this will calculate the difference between current value and the previous. So our bar chart starts on day 2, with the difference in sales between day 2 and day 1. You can change the comparison (Next, First, Last) by clicking on the drop-down menu once more and choosing "Relative To".

### Students Do - Calculations (10 min)

### Everyone Review Calculations

### LUNCH BREAK

### Maps

* We'll be working with our global orders dataset we worked with last class.
* First, note that on the Data Source tab, fields like City and State have been assigned to a geographic type. This is called a "role" (so these fields have a [Geographic Role](https://onlinehelp.tableau.com/current/pro/desktop/en-us/maps_geographicroles.html)).
* When we have fields that are assigned geographic roles, Tableau also generates two new measure: Latitude and Longitude (both "generated") from the dataset.
* Double-click on **Latitude** and **Longitude** fields to add them to the appropriate shelves. Longitude belongs in the Columns shelf because the longitudinal lines are vertical. Latitude goes on the rows because those rows are horizontal.
* Add State to the Detail mark, and Profit to the Color mark. This will give you a map of states, colored by profit!
* Let's create a calculated field to give us a binary classification to profitability, and color states by that, instead.
* We can customize the layers of our map, and even add custom layers that come with Tableau (e.g. census data) to our map.
* Go to the Map menu at the top, and choose the **Map Layers** option. This will bring up a set of options to let us modify our map layers.
* Under the **Data Layer** section, add Population Growth %. Hit the 'x' in the top-right corner of this box to exit the Map Layers options. Now, remove Profitability from the Marks section (we had color assigned to Profitability just before), and drag the Profit measure into the Size mark. Now, we have the population growth layer below a set of markers sized according to the profit for that state.

### Students Do - Exercise 7 (10 Min)

### Students Do - Exercise 8 (10 Min)

### Everyone Do - Review Map Exercises

### Instructor Do - Dashboards

* We can create multiple visualizations on the same page by creating a new Dashboard (middle option of the items in the bottom-right).
* In the Dashboard menu, choose the Actions selection.
* Add a new action, a Filter.
* Keep all defaults, except the "Run action on" option. Choose "Select" from that list. This will let us filter values according to selections users make on the dashboard. If I click on Texas in the top chart, for instance, the bottom chart will update to data for Texas only.
* Adjust charts by clicking on the "More options" menu (bottom option in the options that appear on the right when you select the chart), and set the chart to "Floating". This will enable you to drag and drop the chart anywhere. There are a few related positioning options you can set here.

### Students Do - Dashboards (10 min)

### Everyone Do - Review Dashboards
