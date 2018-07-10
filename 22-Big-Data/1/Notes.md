## 22.1 - Big Data with MrJob, Hadoop and Spark

### Goals

* Understand the MapReduce programming model.
* Understand the pieces of the Hadoop ecosystem.
* Identify similarities and differences between Hadoop and Spark.
* Write MapReduce jobs on your local machine with MrJob.
* Learn how to manipulate data using PySpark dataframes.

### Why?

* So far, we've mostly been doing computation on our local machine. The data we've worked with fits into the (relatively small) memory on our machines. What happens when we have bigger data?
* "Big data" tools are critical for analyzing the mountains of data companies produce! We're going to break "big data" down into its technical components to understand what it's all about.

### Notes

* We will not run Hadoop or Spark on "clusters" of machines today, because there's not an easy way to configure a cluster for free.
* Let me know if there's _anything_ you want to cover during project weeks, as mini-sessions.

### Resources

* [Using mrjob with Amazon EMR (managed Hadoop service)](https://pythonhosted.org/mrjob/guides/emr-quickstart.html)

### Exercises

It is very likely you have Java 8, which is the current major release of Java. Apparently Java 9 [does not play well with Spark](https://gist.github.com/lukewang1024/659ec27847169086dde8677e25156573) yet. Check to make sure you have Java 8 using [these instructions](https://www.java.com/en/download/help/version_manual.xml). If you do happen to have Java 9 installed, [remove it](https://www.java.com/en/download/help/mac_uninstall_java.xml) and [reinstall it](https://docs.oracle.com/javase/8/docs/technotes/guides/install/mac_jdk.html).

Next, you'll need to have the Java JDK installed for some of the work we'll be doing today. [Install that here](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html).

#### Review Big Data PPT - Part 1

#### Review Big Data PPT - Part 2 (MrJob)

#### Everyone Do Exercise 2 - Intro to MrJob

* We won't be using Hadoop to run map reduce jobs. We'll just be solidifyin the concepts of the MapReduce model by running some MR jobs on our local machine.
* We'll be counting the number of times the word "bacon" appears in our `input.txt` file.
* With `mrjob`, all we have to do in a basic job is to define a `mapper` method (takes lines of input and "maps" them to our (key, value) pairs that represent how we're grouping our data - by key - and the computation we apply to that grouping - in this case, just a count of times a given key appears)
* We import the `MRJob` class from the `mrjob` library.
* We create a new `Bacon_count` class that's subclassed from the `MRJob` class (inherits all the class methods and properties of the `MRJob` class).
* Next, we create a `mapper` method that takes three arguments: 1.) this is a class method, so our first arg is `self` 2.) the key that is passed to the mapper, which is going to be blank here, because this is a one-step MR job, and our mapper will not receive any key from a previous step. We use the `_` variable to indicate that this is a throwaway variable: we won't be using it here. 3.) Our mapper method will process a single line of input from our file at a time.
* For every word in our line, we ask: is the word bacon? If so, `yield` a key-value pair of `"bacon", 1`. Think of `yield` here as our return statement. [More about `yield` here](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do) [and here](https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/).
* The `reducer` function takes the output of our mapper jobs - a particular key and a list of values (here, counts) associated with that key  - and sums up the counts.
* Run this script like so: `python bacon_counter.py input.txt`
* Note that `mrjob` is handling a few things behind the scenes: splitting our input file into lines that our `mapper` method runs on, combining the results of our mapper operation for our `reducer` to aggregate, etc.
* Finally, in our `if __name__ == "__main__":` block (if this file is being run as a Python program, vs. being imported), we run `Bacon_count.run()` to run the job.

#### Everyone Do Exercise 3 - Find the number of hot days in Austin in 2017

* Here, we want to find the number of hot days across weather stations in the Austin area, broken out by weather station.
* So we don't care about a specific key, like in our bacon example, but all keys.

#### Students Do - Exercise 4 - Counting Snow Days in Austin (15 min)

#### Review Spark section of PPT

* [A good overview of RDDs](https://jaceklaskowski.gitbooks.io/mastering-apache-spark/content/spark-rdd.html)

#### Everyone install PySpark

* PySpark: Python API for interacting with Spark.
* Enter into your virtual environment
* `pip install pyspark`
* This installs the Python modules necessary to work with Spark, and installs the `pyspark` program locally to run Spark on your computer.

#### Instructor Do - Introduction to Spark DataFrames

* `SparkSession` is the class that helps us instantiate new Spark apps. All interactions will happen with the object we use to create our session.
* Conceptually, Spark DataFrames are similar to Pandas DataFrames, but with Spark, the data is distributed across (potentially) different machines.
* Spark DataFrames hold data in a column and row format where each column represents a variable and each row represents a data point.
* When loading JSON data, the schema may not always be correct, so spark will let you import types and manually set the schema.
* [`StructField`](https://spark.apache.org/docs/1.1.1/api/python/pyspark.sql.StructField-class.html) accepts three fields: 1.) the name of our field, 2.) the type of field (e.g. `IntegerType`, `StringType`), and 3.) whether or not the fields can be null.
* A `StructType` is composed of a list of `StructField`s.
* Given a Spark `DataFrame`, we can show the data in that DataFrame using the `.show()` method.
* The `.withColumn()` method enables us to add new columns, or replace existing ones.
* If you've performed some computation and want to convert the grouped / summarized results into a Pandas DataFrame, you can use the `toPandas()` method. Note that you should only do this for smaller DataFrames (otherwise you might create a DataFrame that's GB in size)
* [A good reference on the company that primariy develops Spark](https://docs.databricks.com/spark/latest/dataframes-datasets/introduction-to-dataframes-python.html)

#### Students Do - Spark DataFrames (15 min)

* [Spark Python API docs](http://spark.apache.org/docs/latest/api/python/index.html)

#### Everyone Review - Spark DataFrames

#### Instructor Do - PySpark DataFrame Filtering

* The `filter()` method of a DataFrame allows more data manipulation, which takes arguments similar to SQL WHERE conditions. Here filter is grabbing all wine that has a price less than 20.
* The `select()` method takes a list of columns to show from a given DataFrame.
