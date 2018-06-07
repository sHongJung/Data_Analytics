# R holds many similarities to Python
# Lets look 3 of the 5 at the atomic (holding one value) data types

# Numeric
a <- 3
b <- 3.1415

# Character
c <- "This is a string"
d <- "Yet another string"

# Boolean
e <- TRUE
f <- FALSE
g <- T
h <- F

# The other 2 atomic types are integer and complex (think imaginary numbers)

# The vector is the main workhorse of R
# A vector contains a homogenous set of data elements of the same type
petz <- c("cat","bird","dog","snake","rat","fish","sugar glider","venus fly trap","rock")
junos_pets <- c("robots", "slinkys", "AIs", "jellyfish")
petnumericvec <- 1:length(petz)

# Numeric vectors can be operated over enmass
petnumericvec2 <- petnumericvec**3

# The c stands for concatinate
# Vectors can be combined using another concatinate function
all_petz <- c(petz, junos_pets)

# Vectors can be looped through
for (animal in petnumericvec){
  print(c(animal,petz[animal]))
}

# List are similar to python dictionaries
shoplist <- list("Crowly's Pet Emporium"=c("cats","dogs","lizards"),
                 "Miss Ava's Flighted Fancy"=c("parrots","finches","fish","turtles"),
                 "Steve's Discount Dogs"=c("poodles", "terriers", "bulldogs", "wolves"),
                 "Juno's Oddities"=junos_pets)

# You can inspect the names of a list with the names function
names(shoplist)

# Use brackets to get a signle value sublist
shoplist["Crowly's Pet Emporium"]

# Or use a vecctor to get a sublist of the items that you want
subshoplist <- shoplist[c(1,3)]

# Use double brackets to get just the values
shoplist[["Crowly's Pet Emporium"]]

# Or use a dollarsign
# Note the backticks if using this method when there are spaces in the name
shoplist$`Crowly's Pet Emporium`

# if statements can be applied much like you would do in Python
for (animal in petnumericvec){
  if (nchar(petz[animal]) > 3){
    next
  }else{
    print(petz[animal])
  }
}

# Functions work much like they do in Python
petshop <- function(petname){
  set.seed(sum(utf8ToInt(petname)))
  # Tells you the best pet for a given petname
  namevec <- c("cat","bird","dog","snake","rat","fish","sugar glider","venus fly trap","rock")
  return(paste("If you want to name your pet", petname, "it should be a", sample(namevec,1)))
}