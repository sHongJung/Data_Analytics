# Piping

* Piping (provided by the `dplyr` package loaded by the `tidyverse`) allows for the ceation of robust data pipelines.
* Simply put function piping takes the output of the previous function and sets it to the first argument of the second function.
  * Note: There are other more niche piping techniques (such as `%<>%` which is overwrite the input and `%$%` which  allows for explicit reference to columns in a `Tibble`), but in the interest of time only the most common piping method is being taught. 
* In order to illustrate the utility of function piping, it's suggested to contrast cases without piping vs cases with piping.
* **Instructor DO**: Demonstrate the advantahe that pipelines confer in simplicity of altering your code
  * All that it takes is a `#` to comment out a single line rather than having to surgically remove a function.
    ![pipingutil][pipeutil]

## When not to use function piping

Pipes are a great _convenience_, but there are cases in which they can make life more difficult.

* When writing long sections of code, if you find that you have over 10 pipes in a single pipeline, the common sentiment is to break that out into smaller pipes that set their output seperate variables. This is because pipes can mask bugs in your code and make debugging more difficult
* When writing packages in R, it is generally frown upon to use pipes in your code because again, they make finding bugs that much more difficult

[pipeutil]: ../../../../Images/Piping_Util.png
