library(tidyverse)

ufo <- read_csv("ufo.csv")

ufo %>% head()

# Count the total # of records in our ufo tibble
ufo %>% count()

# Distinct number of states for which we have UFO sightings
length(ufo$state %>% unique())

# Average duration of sighting, by state, ordered descending
ufo %>% 
  group_by(state) %>% 
  summarise(avg.duration = mean(`duration (seconds)`)) %>% 
  arrange(desc(avg.duration)) 

# Number of sightings by state
ufo %>% 
  group_by(state) %>% 
  summarise(number.sightings = n()) %>% 
  arrange(desc(number.sightings))

# Number of sightings by shape of UFO
ufo %>% 
  group_by(shape) %>% 
  summarise(shape.count = n()) %>% 
  arrange(desc(shape.count))
