# Dependencies
from spread import variance, standard_deviation, zipped_z_scores


def summarize(title, arr):
    print("Summarizing {}".format(title))
    print("Variance: {}".format(variance(arr)))
    print("Standard Deviation: {}".format(standard_deviation(arr)))
    print("Z-Scores: {}".format(zipped_z_scores(arr)))
    print("======")


# Prices of random electronics at Best Buy
prices = [4, 425, 984, 2932, 49]
summarize("Prices", prices)

# Ages of students in bootcamp
bootcamp_classroom_ages = [27, 35, 42, 52, 36, 28]
summarize("Bootcamp Ages", bootcamp_classroom_ages)

# Ages of children and parents at child's party
birthday_party_ages = [6, 5, 6, 6, 35, 34, 42]
summarize("Birthday Party Ages", birthday_party_ages)

# Test score from a 2nd grade geography test
geo_grades = [87, 89, 91, 93, 95]
summarize("Geograph Grades", geo_grades)

# Test scores from a graduate quantum mechanics midterm
quantum_grades = [63, 63, 98, 13, 58, 13, 8]
summarize("Quantum Mechanics Grades", quantum_grades)

# Prices
summarize("Prices", [30, 31, 31, 32, 32, 40, 41, 41, 1000])
