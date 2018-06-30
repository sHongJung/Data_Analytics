## 21.1 - Introduction to Machine Learning with Linear Regression

### Goals

* Apply linear regression to datasets using `scikit-learn` (a popular Python machine learning library).
* Understand the difference between linear and non-linear data.
* Understand how to quantify and validate linear models.
* Understand how to apply scaling and normalization as part of the data pre-processing step in machine learning.

### Notes

* There will be no HW on machine learning. *Phew*.
* You'll be required to use machine learning in your final project.

### Resources

* [scikit-learn tutorials](http://scikit-learn.org/stable/tutorial/index.html)
* [Andrew Ng's Machine Learning Coursera course](https://www.coursera.org/learn/machine-learning)
* [An introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/)

### Exercises

#### Slideshow on Machine Learning (15 min)

* Artificial Intelligence (AI) concerns systems that can think or act like humans (rational, intelligent thought).
* AI has a number of disciplines, including natural language processing, automated reasoning (drawing new conclusions from existing information), and machine learning.
* Machine learning enables us to detect patterns and adapt to new circumstances.
* Arthur Samuel: "the ability to learn without being explicitly programmed".
* Estimator: our rule for calculating our predicted value given our data.
* [scikit-learn cheatsheet for choosing the right estimator](http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html)

#### Instructor Do - Univariate Linear Regression

* We're going to start our journey into machine learning with linear regression.
* This is the first estimator that data scientists typically use, because it's fast to run and simple to interpret.
* We'll be using `scikit-learn` to run machine learning algorithms: `pip install sklearn` (you may also need to `pip install scipy`).
* Univariate = we have a _single_ variable X that we're using to predict some response variable Y. There is only one attribute we're measuring (e.g. the square feet of homes) that we're using to preduct the value of another variable (e.g. the price of the home).
* This variable X is commonly referred to as a "feature".
* The [`make_regression`](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html) function from `sklearn` is being used here to generate a set of random data that we'll use in a test model.
* Linear data: the ratio between the change in x and the change in y must be constant. Can be modeled using our standard linear equation.
* Non-linear data: data that cannot be modeled with a linear equation.
* Given linear data, we can fit a linear model to our data using a technique called linear regression.
* Linear regression gives us a "best fit" line.
* QUESTION FOR THE CLASS: how do we draw a line through our data?
* Technique: minimize the distance between the square of the difference between the point and the estimator function (the line that predicts that point).
* This technique helps us achieve *best* fit, which is a lot different than *perfect* fit!
* Given this estimator, we can predict the value of Y given a _new_ value of X.
* We must *fit* our model (a general function for producing lines) to our data (we need a specific line function that predicts values of Y given values of X).
* We'll use the `LinearRegression` model from `sklearn` here.
* We'll then create the model and fit it to the data using `model.fit(X, y)`. This process is also referred to as "training" the model.
* `model.coef_` gives us the coefficient (the slope) of our line function. `model.intercept_` gives us the y-intercept.
* `model.predict(new_x_value)` returns the predicted value of y, given our line function.

#### Students Do - Linear Regression (15 min)

* See [this explanation](https://stackoverflow.com/questions/18691084/what-does-1-mean-in-numpy-reshape) of `reshape(-1, 1)`.
* The use of `np.array` with the multi-dimensional looks a bit strange. The [`predict` method of an estimator](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.predict) expects numpy arrays of shape `(n_samples, n_features)`. In this example, we have only 1 sample with 1 feature.

#### Everyone Review Linear Regression (10 min)

#### Instructor Do: Quantifying Regression (10 min)

* We want more than just visual confirmation that our model is correct. We need some mathematical quantification of our model accuracy!
* Our model will never be perfect. But we need some way to compare models to assess which are better than others.
* ["All models are wrong but some are useful"](https://en.wikipedia.org/wiki/All_models_are_wrong)
* Mean squared error (MSE) and the R squared score (R^2) are two ways to assess the accuracy of our models.
* MSE: the mean of the "error" (difference) between the model (our line) and the actual y values at each value of X. On average, how much does our model deviate from the actual values in our test data?
* MSE provides a measure of fit in the units of the quantity to be estimated. Our MSE for home prices might be $1000. 
* R^2 provides a different measure of model accuracy: a value between 0 and 1 (1 is better) that quantifies the proportion of variance in the data that is "explained" by the model.
* In data that cannot be perfectly modeled using a line, there will always be some natural variability that cannot be explained using a straight line estimate. 
* A "good" R^2 score depends on context. If you have close to perfectly linear data, an R^2 score for your model should be high. If you have more complex data (real life) that cannot be perfectly modeled using a line, lower R^2 scores might be OK.
 * How well does our model do on real data? 1.) split your data into "test" and "training" subsets. 2.) Fit the model using the training data. 3.) Score and validate the model using the test subset.
 * [Docs on the `train_test_split` function in sklearn](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html).

#### Students Do - Brains (15 min)

#### Everyone Review Brains (10 min)

#### Instructor Do - Multi-feature linear regression (10 min)

* With this one, follow the concepts.
* Remember that a feature is an input variable that we use to predict a response variable.
* So far, we've been using only a single feature to predict our response variable.
* We'll now consider multiple features to predict our response.
* Example: before, we used just the # of square feet of a home to predict its price. Now, we may want to use the # square feet and # of bedrooms.
* We can still use our `LinearRegression` model and fit it to our data using `model.fit(X, y)`, where X is an array containing data points tied to _all_ of our features.
* Difficult to visualize the linear relationship between multiple features and a response variable. So we plot "residuals" - the difference between the true values of y and the predicted values of y - on a two-dimensional plot to visualize this.
* We can still visualize the relationship between 2 features and a response variable in 3 dimensions. [Here's a visualization](https://giphy.com/gifs/BN2EIboh88OLfZTY5B/fullscreen), with [the code](https://github.com/dylburger/jupyter-notebook-examples/blob/master/Visualizing%20Multivariate%20Linear%20Regression.ipynb).
* Note that we still have an R^2 score for our model that you can find using `model.score()`

#### Students Do - Beer Foam (15 min)

* [Why does R^2 always increase when we add more variables?](https://www.quora.com/Why-when-the-number-of-variables-increases-does-the-R-square-also-increase-in-linear-regression)

#### Everyone Review Beer Foam

#### Instructor Do - Data Pre-processing

* Regression helps us predict a response variable from one or more numeric features. 
* These features _must_ be numeric. If we have categorical data, we must convert that categorical variable into a numeric value.
* Binary encoding allows us to take a particular field, for example gender, and produce new columns in our dataset that map to each value of that categorical value.
* We'll create a column **per value of the categorical variable**. In our dataset, we have two genders: Male and Female. So we want to create two new fields: "is male?" and "is female?", each to indicate whether this particular record is a Male (1 for the "is male?" field, 0 for the "is female?" field) or Female (1 for the "is female?" field, 0 for the "is male?" field).
* `pandas` provides us a function to do this: `get_dummies()`. This takes as arguments 1.) the DataFrame you're processing and 2.) the columns for which you want to produce dummy (or "indicator") variables.
* If we don't pass columns to `get_dummies()`, `pandas` will convert _all_ columns of type `object` or `category` to new dummy columns.
* Note that the `get_dummies()` function modifies the DataFrame in place, hence we copy it before we run this function so we don't modify our original DataFrame.
* For some of the algorithms we'll deal with in ML, they will perform better if our data is normalized (in this particular case, normalization refers to the process of adjusting the values of our data to be normally-distributed with a mean of 0 and a variance of 1).
* The `StandardScaler` class from the `sklearn.preprocessing` library provides functions to scale our features and response variables using this algorithm (normal distribution with mean 0 and variance 1).
* After scaling your data, you can fit your model to the scaled data and predict values from there.

#### Appendix

* [Bias and the bias-variance tradeoff](https://ml.berkeley.edu/blog/2017/07/13/tutorial-4/)
* Page 65 of Introduction to Statistical Learning (PDF link above) also has a good discussion of bias.
