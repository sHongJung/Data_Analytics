# The Heart of Class

## Instructions

* In this activity, you will be tasked with first defining a Python class, then using that class to create objects.

### Part I

* Define a Film class in Python. This class will have the following attributes: **title, length, year of release, and language.**

* Use your Film class to create two movie objects of your choosing, with the correct attributes. (You can consult Wikipedia or IMDB, if you like.)

  * For example, `star_wars.length` should yield `121`, and `star_wars.language` should yield `English`.

### Part II

* Create an Expert class with `name` and `specialty` attributes, and a `boast()` method. The `boast()` method should be able to take a Film object as an argument, and print out its `title`, `length`, and `year` of release.

  * For example, if we create an object named `ebert` belonging to the Expert class, `ebert.boast(star_wars)` should print out a series of statements like the following:
  
  ```
  Hi. My name is Ebert. 
  I know a lot about Star Wars. 
  It is 121 minutes long. 
  It was released in 1977. 
  And its language is English.
  ```

### Extras

* If you finish early, you may want to read further about Python classes here: [https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/](https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/)
