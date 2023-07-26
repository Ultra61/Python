class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(str(self.name) + " is now sitting")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(str(self.name) + " rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 4)

print("My dog's name is " + str(my_dog.name))
print("My dog is " + str(my_dog.age) + " years old")

my_dog.sit()
my_dog.roll_over()

