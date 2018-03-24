# Review Questions

This document contains review questions for Git basics.

## Instructions

For the diagramming problems below, either **draw your solutions on paper**, or use the interface provided at [Git Viz](https://peleke.github.io/git-viz/).

#### Overview

**Problem**

Consider the example from lecture, where we created a branch for our data analysis. Why did we create a new branch for this? Why _not_ simply do this on `master`?

**Problem**

Write down two advantages to creating branches instead of working directly on `master`.

### Branching

For the problems below, consider the following commit history.

```
(master) | [m1] -> [m2] -> [m3] -> [m4]
```

- - -

**Problem**

Draw a new branch, called `plotting_data`. It should branch from the second commit to `master`.

**Problem**

When you first create `plotting_data`, are the files on that branch the same as the files in `[m1]`? In `[m2]`? Why, or why not?

**Problem**

Add two commits to the `master` branch.

**Problem**

Add two commits to the `plotting_data` branch, named `[pd1]` and `[pd2]`.

**Problem**

Are the files in `[pd1]` and `[m3]` the same? Why, or why not?

## Merging

**Problem**

Merge `[pd2]` with `master`.

**Problem**

Explain how this merge changes the files in `master`.

- - -

For the problems below, consider the final commit history from lecture.

```
(master)        | [m1]-[m2]-[m3]- - -- - -- - -- - ---[m4]
                              \               / (M)
(plotting_data) |              \-[pd1]-[pd2]-/
```

- - -

**Problem**

Assume the root project directory looks as follows at each commit:

```
[m3]
root/
  |_analyze_data.py
  |_clean_data.py
  |_output/
    |_cleanedRideData.csv
  |_Resources/
    |_rideData.csv

[pd2]
root/
  |_analyze_data.py
  |_clean_data.py
  |_helpers.py
  |_plot_data.py
  |_output/
    |_cleanedRideData.csv
    |_plots.pdf
  |_Resources/
    |_rideData.csv
```

**Problem**

Add a commit after `[m3]` on `master` (assume this updates `clean_data.py`, but doesn't change the directory structure). Keep the merge commit.

**Problem**

When we merge `master` and `plotting_data`, which version of each file do we get? 

Draw the directory structure for the last commit to `master`—after the merge—and label each file with the branch it comes from. Assume that the only files changed on `plotting_data` were `helpers.py` and `plot_data.py`.

- - -

### Copyright

Coding Boot Camp © 2017. All Rights Reserved.
