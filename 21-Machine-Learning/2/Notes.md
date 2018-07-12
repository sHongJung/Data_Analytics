## 21.2 - Machine Learning - Classification

### Goals

* Understand how to calculate and apply the fundamental classification algorithms: logistic regression, SVM, KNN, decision trees, and random forests.
* Learn how to quantify and validate classification models including calculating a classification report.

### Notes

* Today will be a bit more challenging than Wednesday's work. Focus on the concepts first, code second.
* There's not a good answer for "which algorithm should I choose?" The [sklearn cheat sheet](http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html) can be a helpful guide.
* Some algorithms naturally lend themselves to binary classification or multi-class classification. We'll talk about those more today.

### Exercises

#### Instructor Do - Data Pre-processing

* Regression helps us predict a response variable from one or more numeric features. 
* These features _must_ be numeric. If we have categorical data, we must convert that categorical variable into a numeric value.
* Binary encoding allows us to take a particular field, for example gender, and produce new columns in our dataset that map to each value of that categorical value.
* We'll create a column **per value of the categorical variable**. In our dataset, we have two genders: Male and Female. So we want to create two new fields: "is male?" and "is female?", each to indicate whether this particular record is a Male (1 for the "is male?" field, 0 for the "is female?" field) or Female (1 for the "is female?" field, 0 for the "is male?" field).
* `pandas` provides us a function to do this: `get_dummies()`. This takes as arguments 1.) the DataFrame you're processing and 2.) the columns for which you want to produce dummy (or "indicator") variables.
* If we don't pass columns to `get_dummies()`, `pandas` will convert _all_ columns of type `object` or `category` to new dummy columns.
* Note that the `get_dummies()` function modifies the DataFrame in place, hence we copy it before we run this function so we don't modify our original DataFrame.
* For some of the algorithms we'll deal with in ML, they will perform better if our data is normalized (in this particular case, normalization refers to the process of adjusting the values of our data to be normally-distriuted with a mean of 0 and a variance of 1).
* k-nearest neighbor, for instance, uses the actual distance between points to determine "closeness". If the units of one feature are much larger than the units of another, the "distance" between points will be determined primarily by the feature with smaller units (shorter distance). [Reference here](https://stats.stackexchange.com/a/121898).
* The `StandardScaler` class from the `sklearn.preprocessing` library provides functions to scale our features and response variables using this algorithm (normal distribution with mean 0 and variance 1).
* Plot the data before and after normalization!
* After scaling your data, you can fit your model to the scaled data and predict values from there.

#### PPT on Logistic Regression

#### Exercise 1 - Logistic Regression

* Instead of using the `make_regression` function to generate data, we'll use `make_blobs`. 
* This generates two "clusters" of data.
* By default, `make_blobs` generates an array with two features for our X data, and a set of binary labels for our `y` data.
* We can visualize these clusters by passing in the value of our labels (`y`) as the color of the points on our scatter plot (`c=y`).
* As with linear regression, we still want to split our data into a training and a test set!
* Note the use of the `stratify` parameter, which first splits our data into groups by label (groups of data tied to the 0 label, and the 1 label), and makes sure we sample the same percentage of records from each sub-population. If we had a lot more records with label 0, and then just did a random sample, we'd have a lot more records tied to label 0 in our model, and this could affect its accuracy.
* After this, **our flow will be exactly the same as before: choose our model, fit our model to data, predict new values**.
* We use the `LogisticRegression` model here, instead of `LinearRegression`.
* The `score` returns something slightly different than before: here, it calculates the mean accuracy of the classifier (how many times do we correctly predict the outcome, of the number of predictions?)

#### Students Do: Gender Voice Recognition (0:20)

#### Everyone Review Gender Voice Recognition

#### Instructor Do: Decision Trees & Random Forests

* A decision tree creates a set of logical conditions that will collectively evaluate to True or False. We move down the appropriate branch and keep testing conditions until we establish a class.
* Random forests result from collections of decision trees.
* We build a number of decision trees using only a random sample of the features to predict the class of the response variable.
* We then ask the question, "if we compare all these trees, are there features that consistenly predict the response variable?" A random forest is built by, conceptually, "averaging" these trees.
* FYI: in the `Ins_Decision_Trees` Jupyter notebook, you will not be able to generate the tree in the final cell without installing the `graphviz` program and Python module. Do not worry about this.
* How to choose the number of trees? ["You can run as many trees as you want"](https://www.stat.berkeley.edu/~breiman/RandomForests/cc_home.htm#remarks) (from the guys who invented random forests).
* Feature importance: roughly, of the number of nodes, how many times is this feature used to make a decision (to "split" a node)?
* We can get the importance of features in a random forest through the attribute `rf.feature_importances_`.

#### Students Do: Trees (0:15)

* Note: don't worry about the `graphviz` piece.

#### Everyone Review Trees

#### Instructor Do - KNN (K-Nearest Neighbors)

* Review PPT for information about how KNN works conceptually.
* Why do we have to normalize our data using the `StandardScaler` model? [Reference 1](https://stats.stackexchange.com/a/121898) [Reference 2](https://stats.stackexchange.com/questions/287425/why-do-you-need-to-scale-data-in-knn/287439).
* Especially for binary classification problems (two potential outcomes), k is always odd so that we don't have ties between groups (When k = 2, for instance, the two closest points could be one from group 1 and another from group 2).
* With smaller k, there's generally a lot of noise because random points of data may influence the closest neighbors (I could have clusters of 3 or 4 random points in one class that are nearest to a given point, but those are just outliers. When k is larger, I'll correctly classify the point because I'm looking for more nearest neighbors).
* The choice of k should, primarily, maximize the accuracy of the model when run on our test set. Another rule of thumb: choose k to be the square root of the number of records in your data (because some math that I haven't read about).
* But if the difference between the accuracy between two k is small, choose the lowest k that has a relatively high accuracy. knn can be computationally expensive for large, large datasets, so choosing a smaller k will get you an answer faster (with a very small sacrifice in model accuracy)! Again, this choice all depends on your data.

#### Students Do - KNN

#### Everyone review KNN

#### Instructor Do - Linear SVC (Support Vector Classifier) and SVM (Support Vector Machine)

* A classifier
* Classes must be separable by a linear boundary
* Support Vector Machines are intended for binary classification (two classes).
* The SVC class (Support Vector Classification) will be our base model for this exercise.
* This supports a number of different "kernels", which are just functions that recognize patterns (similarity) in our data. We'll be using the linear kernel.
* [This reference](https://medium.com/machine-learning-101/chapter-2-svm-support-vector-machine-theory-f0812effc72) provides a good conceptual overview of SVM.
* Precision: of the results we marked cancer, how many are actually cancer? A measure of the quality of the algorithm.
* Recall: of all the results that are _actually_ cancer, how many did we correctly identify? Are we missing a lot of cancer?
* The [Wikipedia page](https://en.wikipedia.org/wiki/Precision_and_recall) on precision and recall provides a pretty good description.
