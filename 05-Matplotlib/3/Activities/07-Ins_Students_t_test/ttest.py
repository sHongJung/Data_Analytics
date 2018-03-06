# Dependencies
import numpy as np
import pandas as pd
from scipy import stats

# Read data
housing_data = pd.read_csv("./Resources/housing_data.csv")
housing_data = housing_data.sample(frac=1).reset_index(drop=True)

# Create two samples
s1 = housing_data.iloc[0:19, 13]
s2 = housing_data.iloc[20:40, 13]

(t_stat, p) = stats.ttest_ind(s1, s2, equal_var=False)
print("t-statistics is {}.".format(t_stat))
print("p-value is {}.".format(p))
