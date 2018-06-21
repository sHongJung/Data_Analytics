## 20.1 - Intro to Tableau

### Goals

* Import data from CSVs / XLSX files into Tableau.
* Perform joins between data sources.
* Create basic visualizations in Tableau.
* Customize these visualizations.
* Create story boards.

### Why?

* Tableau is one of the many tools used by the *business* to analyze data, vs. Jupyter notebooks, which typically wouldn't be shared with "normal" people. Like Excel, Tableau requires no programming knowledge to use.
* **It's critical to let people answer their own data-related questions**. Without tools like Tableau, people have to ask you  - the master of data - to do every analysis question they might have. No one has time for this.
* Like Plotly and Carto, you can create advanced visualizations in Tableau with little work.

### Notes

* I know some of y'all use Tableau at work or have extensive experience with it. If I don't know the answer to a question and you do, shout it out!
* So many of the features of Tableau are learned through discovery. We're going to do more student exercises than normal today to get y'all interacting with Tableau as much as possible.
* [Tableau keyboard shortcuts](https://www.tableau.com/about/blog/2016/8/take-note-these-10-handy-tableau-shortcuts-57561)

### Exercises

#### Intro to Tableau

* **You can create powerful visualizations without writing a line of code**. We like writing no code.
* We see a few of the visualizations we've created before here.
* You can share visualizations easily with others in the public (or with others in your org). You can embed Tableau visualizations in a web page

#### Students Do - Install Tableau

* We'll be using Tableau Public
* Tableau Public limits the data sources you can connect to (no SQL DBs), requires that you share your data sets publicly on the Tableau Public Server, and limits the number of rows of data you can work with (I belive 1MM rows).
* **Install here**: [https://public.tableau.com/en-us/s/](https://public.tableau.com/en-us/s/).

#### Instructor Do - Connecting to Data (exercise 1)

* Tableau can connect to "flat files" (CSVs, JSON, etc.) or to a server (databases, Google Sheets, etc.)
* Since Tableau connects to many varied data sources, there's no need for you to translate these data into a common format, e.g. a Pandas DataFrame, in order to join them together.
* You can drag the file you want to visualize into Tableau and it will create a new connection to the file.
* Since our Excel workbook has multiple sheets, we must work with one sheet at a time. Drag the Orders sheet into the section to the right.
* After dragging, we see a preview of the dataset in the table below.
* **Filters** allow us to filter rows based on some condition. These conditions can be quite complex. **Click the Add button under Filters in the top-right corner**.
* The filter menu changes as the type of the data changes. Choose the Order Date column and see how the menu changes as a result.
* Note: we cannot edit the values of cells, but we can add new columns that are the result of functions applied on existing columns. We'll see how to do this later.

#### Instructor Do - Creating our first visualization

* **Question**: does anyone know the difference between measures and dimensions?
* Measures are metrics: the data you want to visualize.
* You split measures by dimensions: dimensions are categorical data used to split and group data.
* **Numbers can operate as dimensions**: e.g. you can split sales by the number of orders a customer has made in their lifetime ("Users who made 1 order contribute to 80% of our sales. Users who made 2 order contribute 10% of our sales. Etc."). Age is another good example: age can be both a measure (you want to understand the average age given a certain grouping) and a dimension (you want to count the number of Americans _grouped by_ age).
* When we drag *Quantity* into the Columns group, Tableau automatically sums data. We'll talk about this in more detail.
* You don't have to drag. You can move your selection using the up and down arrow and press Enter to add the field to the appropriate "shelf" (the section of the UI that you can place pills into).
* These measures and dimension icons are called "pills" in Tableau.
* We can add *Market* to the Columns group to break out data by Market along the column "axis". 
* Click on the "Show Me" header tab in the top-right to choose relevant visualizations. Note that Tableau will require specific criteria for each visualization (making it difficult to create a visualization that wouldn't work given the measures and dimensions present).
* If we create a new worksheet (click on the left-most plus sign at the bottom of the window), and add Sales to the Rows, a vertical bar chart is displayed. This displays the sum of Sales across out entire dataset (we haven't added any dimensions).
* What if we wanted the count, or the average of the Sales field given some grouping? We can change the measure applied to this field (Sum) by clicking on the drop-down menu on the field and choosing the "Measure".
* Let's add the Order Date as a column to give us a basic line chart of Sales broken out by year.
* We can drill one level deeper - to get the breakout by (Year, Quarter) - by clicking on the plus-sign to the right of the YEAR(Order Date) field.
* What's going on here? Tableau chooses to break out datetime data by the least granular level (Year). 
* There are a lot of these neat features. Explore on your own to discover more!

### Students do Exercise 3 - 15 min

### Everyone Review Exercise 3

* Note that my solution is in a "Tableau Packaged Workbook" (twbx) format. You can export your own workbooks (File -> Export Packaged Workbook)
* Ctrl Z - Undo
* Ctrl Y - Redo

### Students do Exercise 4 - No Shows - 20 min

* HINT: find out how to convert measures to dimensions.

### Instructor Do - Joins and Splitting

* As we remember with SQL, joins can be difficult to conceptualize and to perform. Tableau provides a visual interface for performing joins.
* Load the XLSX file in the `05-Ins_EasyJoins/Resources` directory. Pull in the Orders sheet, then the People sheet.
* Tableau will immediately merge these two datasets using an inner join on the columns that contain matching values.
* Clicking on the joined circles tells us 1.) the type of join and allows us to change it, and 2.) the column on which the two sheets are joined.
* These two sheets are part of the same data source, but you can join data across data sources, too!
* Near the top-left of the window, click "Add" and load the `GlobalSuperstoreReturns2016.csv` CSV of data in the `05-Ins_EasyJoins/Resources` directory this time.
* Tableau will attempt to join these, again using an inner join, this time on Order ID.
* Splitting allows you to split a text field by a delimeter, like we've done in Python before.
* Right click on the field name in the Data Source UI, choose "Custom Split", and choose the field # you want to grab after the field is split by the delimeter. e.g. if you had a field "CA-123", splitting by "-" yields "CA" and "123", the 1st and the 2nd fields, respectively.

### SKIP FIFA

### Instructor Do: Sizing, Coloring, and Labels

* Under the `Marks` section to the left of the chart, you can change things like Color, Size of each data point, attach data labels, and adjust the text of the tooltip that appears on hover.
* For scatter plots and other charts, adding a dimension to detail allows us to break out individual data points by that dimension (try this in the next exercise). See [this reference](https://www.interworks.com/blog/rcurtis/2016/03/21/tableau-deep-dive-lod-introduction-detail).

### Students Do - The Ultimate Candy Exercise (10 min)

### Everyone Do - Review Ultimate Candy

### Instructor Do - Storytelling with Stories

* Tableau allows you to create collections of charts, which they call Stories.
* Click on the plus sign at the bottom right of the options in Tableau to create a new story.
* A story is an ordered collection of existing dashboards. You can drag dashboards available in your current Tableau session into the window to add it to the story.
* Double-click on the text at the top to add a new caption to this dashboard.
* At the top-left, you can add another section to your story by adding a "New story point". You can either duplicate an existing story point or create a blank one.
* Use the "Drag to add text" option to add an annotation to a specific dashboard.
* Check out the Layout tab near the top-left: if you don't want to add captions to headline your dashboards, you can use ordered numbers or just dots. Sometimes the captions may take away from your story, so it's worth considering whether you need them.

### Students Do - What Degrees Pay? (15 min)
