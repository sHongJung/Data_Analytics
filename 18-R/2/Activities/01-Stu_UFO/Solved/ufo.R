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
  summarise(counts.sightings = n()) %>% 
  arrange(desc(counts.sightings))

# Number of sightings by shape of UFO
ufo %>% 
  group_by(state, shape) %>% 
  summarize(counts = n()) %>% 
  arrange(desc(counts))
