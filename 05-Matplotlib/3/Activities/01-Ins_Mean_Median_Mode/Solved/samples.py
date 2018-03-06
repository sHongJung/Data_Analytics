# Dependencies
from statistics import mean, median, mode, multi_mode

# Prices of random electronics at Best Buy
prices = [4, 425, 984, 2932, 49]
print("Median Price: {}".format(median(prices)))

# Ages of students in bootcamp
bootcamp_classroom_ages = [27, 35, 42, 52, 36, 28]
print("Mean Bootcamp Age: {}".format(mean(bootcamp_classroom_ages)))
print("Median Bootcamp Age: {}".format(median(bootcamp_classroom_ages)))

# Ages of children and parents at child's party
birthday_party_ages = [6, 5, 6, 6, 35, 42, 34]
print("Mode of Birthday Party Ages: {}".format(mean(birthday_party_ages)))

# Test score from a 2nd grade geography test
geo_grades = [87, 89, 91, 93, 95]
print("Mean of Geography Test Scores: {}".format(mean(geo_grades)))

# Test scores from a graduate quantum mechanics midterm
quantum_grades = [63, 63, 98, 13, 58, 13, 8]
print("Median of QM Grades: {}".format(median(quantum_grades)))
print("Modes of QM Grades: {}".format(multi_mode(quantum_grades)))
print(mean(quantum_grades))
