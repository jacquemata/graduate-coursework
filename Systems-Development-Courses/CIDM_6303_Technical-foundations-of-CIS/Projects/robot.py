# Create a Robot class according to the instructions
# import random will have functions useful for this assignment
import random

# Start coding here...
# Define a class called Robot()
class Robot():
    # define a constructor
    def __init__(self, name):
        self.name = name

    # define a method called hello()
    def hello(self):
        print(f"Hi. My name is {self.name}. I can count and sing. And, I have feelings.")

    # define a method called sing()
    def sing(self):
        print("Mary had a little lamb...")

    # define a method called count()
    def count(self, stop_number):
        for i in range(0, stop_number):
            print(i)

    # define a method called how_do_you_feel()
    def how_do_you_feel(self):
        possible_feelings = [":-)", ":-O", ":-(", ":-P"]
        current_feeling = random.choice(possible_feelings)
        print(f"I feel {current_feeling}")


# Test code. DO NOT CHANGE THIS TEST CODE
try: 
    r = Robot("Marvin")
    r.hello()
    r.sing()
    r.count(10)
    r.how_do_you_feel()
except AttributeError as err:
    print("***Test failed***")
    print("Missing a method. Making progress but not done yet. Keep coding and try again.")
    print(err)
else: 
    print("Test successful. Your code passes")