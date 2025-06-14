class Computer:


	def __init__(self):
		self.name="venky"
		self.age =27

c1=Computer()
c2=Computer()
c1.name="Rashi"
print(c1.name)
print(c2.name)
print('''
	Class Definition (Computer):

The Computer class is defined with an __init__ method.

This constructor initializes every new object with:

name = "venky"

age = 27

Object Creation:

c1 = Computer() creates the first object.

c1.name is initially "venky"

c1.age is 27

c2 = Computer() creates the second object.

c2.name is also "venky"

c2.age is 27

Modifying an Instance Variable:

c1.name = "Rashi" changes the name attribute only for c1.

c2.name remains unchanged ("venky"), proving that each object maintains its own copy of instance variables.

Output:

print(c1.name) → "Rashi"

print(c2.name) → "venky"

				''')