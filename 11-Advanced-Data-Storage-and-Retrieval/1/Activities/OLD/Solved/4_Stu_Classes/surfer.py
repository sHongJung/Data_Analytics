# Define a class
class Surfer():
    def __init__(self, name, hometown, rank):
        self.name = name
        self.hometown = hometown
        self.rank = rank


# Create an instance of a class
surfer = Surfer('Kelly Slater', 'Cocoa Beach', 1)

# Print the object's attributes
print(surfer.name)
print(surfer.hometown)
print(surfer.rank)
