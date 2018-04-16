# Define the Surfer Class
class Surfer():

    # Keep track of surfer count as they are created
    surferCount = 0

    # Constructor
    # --------------------------------------------------------------------------------
    # Initialize the surfer and assign each surfer a new surfer count upon creation
    def __init__(self, name, hometown, rank, wipeouts=0):
        self.name = name
        self.hometown = hometown
        self.rank = rank
        self.wipeouts = wipeouts
        Surfer.surferCount += 1
    
    # Class Methods
    # --------------------------------------------------------------------------------
    # Prints what number surfer they are based on when they were created
    def surfer_count(self):
         print("Total surfers shredding waves %d" % Surfer.surferCount)

    # Prints out simple string
    def speak(self):
        print("Hang loose bruh!")

    # Interpolates based on their attributes
    def biography(self):
        print(f"My name is {surfer.name}, I am from {surfer.hometown} and rank #{surfer.rank}, I've wiped out {surfer.wipeouts} times!")

    # Check how many wipeouts and print out a statement
    def cheer(self):
        if self.wipeouts == 0:
            print('I totally rock man, no wipeouts!')
        else:
            print('Bummer bruh, keep on keeping on!')


# Create Surfers
# --------------------------------------------------------------------------------

surfer = Surfer('Kelly Slater', 'Cocoa Beach', 1,)
print(surfer.name)
print(surfer.hometown)
print(surfer.rank)
print(surfer.wipeouts)
surfer.speak()
surfer.biography()
surfer.cheer()
surfer.surfer_count()

surfer = Surfer('John Breezy', 'Spring Lake', 1, 10)
print(surfer.name)
print(surfer.hometown)
print(surfer.rank)
print(surfer.wipeouts)
surfer.speak()
surfer.biography()
surfer.cheer()
surfer.surfer_count()
