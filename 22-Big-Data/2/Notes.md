## 22.2 - More PySpark, Natural Language Processing

### Goals

* Understand natural language processing (NLP) workflow, terminology.
* Reinforce PySpark fundamentals by continuing to work with PySpark DataFrames.
* Apply what we've learned to create a spam filter.
* It's going to take just a little while to get to the punch line (creating our spam filter). Bear with me!

### Why?

* NLP is important in many domains where you're trying to derive meaning from text.

### Notes / Resources

* When Googling questions on PySpark, make sure to start your query with "pyspark" instead of just "spark", since the latter may yield results for the Scala / Java docs.
* [Great article by Google researchers](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/35179.pdf) on tackling natural language problems with big data
* [A thorough resource on machine learning in Spark](https://spark.apache.org/docs/2.1.0/ml-features.html), with lots of resources for the techniques we'll use today

### Exercises

#### PPT - Intro to NLP, slides 1 - 11 (15 min)

* NLP: goal is to process and generate human language.
* Degrees of success in achieving this goal, depending on the problem. NLP does a pretty good job now of spam filtering, spell checking, identifying parts of speech. Medium job at sentiment analysis and translation. Sustained conversation (remember the Turing test!) is hard.
* Tough to convert text into a format the computer can interpret.
* The first step is tokenization: we need to segment text into the units we care about (e.g. words, phrases, sentences)

#### Exercise 1 - Instructor Do Tokenization with PySpark (5 min)

Notes in Jupyter notebook

#### Exercise 2 - Instructor Do UDFs (5 min)

#### Exercise 3 - Students Do NLP tokens (15 min + 5 min review)

Instructions are in Jupyter notebook

#### PPT - Stop Words (5 min)

* [Good resource on stop words, with a few examples of where they might not be useful (specific to information retrieval systems)](https://nlp.stanford.edu/IR-book/html/htmledition/dropping-common-terms-stop-words-1.html)

#### Instructor Do - Stopwords (10 min)

#### Exercise 5 - Student do Food Review NLP (10 min + 5 min review)

Instructions are in Jupyter notebook

#### Instructor Review - N-grams (5 min)

#### SKIP Students Do N-grams

#### PPT - Stemming, tf-idf (10 min)

* Spark does not come with its own stemming algorithm. It's common to use [nltk](http://www.nltk.org/howto/stem.html) (Natural Language Toolkit) for this purpose.
* [tf-idf reference](http://www.tfidf.com/)

#### Exercise 8 - HashingTF (10 min)

* [How to pick the right `numFeatures` with HashingTF](https://stackoverflow.com/questions/44966444/what-is-the-relation-between-numfeatures-in-hashingtf-in-spark-mllib-and-actual)
* [Tradeoffs with using HashingTF and CountVectorizer](https://stackoverflow.com/questions/35205865/what-is-the-difference-between-hashingtf-and-countvectorizer-in-spark)
* [Another article describing both techniques applied in practice](https://towardsdatascience.com/apache-spark-hashing-or-dictionary-d23c0e046a19)

#### Exercise 9 - Students Do HashingTF (10 min + 5 min review)

#### Everyone Do Exercise 12 - Naive Bayes Classifier (30 min)

[Naive Bayes, Why Multinomial Naive Bayes?](http://blog.datumbox.com/machine-learning-tutorial-the-naive-bayes-text-classifier/)
* Key takeaway: multinomial Naive Bayes is used where word frequency (or measures like tf-idf) is imporant (vs. just the presence or absence of a particular word).

#### Students Do Exercise 13 - Yelp Reviews with Naive Bayes (15 min + 10 min review)
