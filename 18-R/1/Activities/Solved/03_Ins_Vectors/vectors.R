# Months of the year
months <- c("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

# Average rainfall/precipitation in NYC during each month
precipitation <- c(3.9, 2.9, 4.1, 3.9, 4.5, 3.5, 4.5, 4.1, 4.0, 3.4, 3.8, 3.6)

# Assign months to precipitation as names
names(precipitation) <- months

# Display precipitation
precipitation

# Display names of precipitation
names(precipitation)

# Access a single member of precipitation by its name
precipitation["Mar"]

# Display summary data of precipitation
summary(precipitation)

# Assign summary to a variable
precipitation_summary <- summary(precipitation)

# Access a feature of summary
precipitation_summary["Min."]
precipitation_summary["Mean"]

# Use double brackets to access only the value
precipitation_summary[["Max."]]

# Display the standard deviation 
sd(precipitation)

# Round SD to two digits
stdev <- sd(precipitation)
round(stdev, 2)

# Determine the length of a vector
length(precipitation)

# Display the sum of a vector
yearly_precipitation <- sum(precipitation)
yearly_precipitation