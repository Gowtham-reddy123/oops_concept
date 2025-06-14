class Computer:
	def __init__(self):
		self.name='Venky'
		self.age= 28
	def update(self):
		self.age=30
	def compare(self,c2):
		if self.age==c2.age:
			return True
		else:
			return False
c1=Computer()
c2=Computer()
if c1.compare(c2):
	print("They are same ")
	
print('''	1.Class Definition:

The Computer class is defined with an __init__ constructor, an update method to change the age, and a compare method to compare the age of two Computer objects.

2.Object Creation:

c1 = Computer() creates the first object. Inside the constructor (__init__), name is set to 'Venky' and age to 28.

c2 = Computer() creates another object in the same way, with name='Venky' and age=28.

3.Calling compare() Method:

c1.compare(c2) calls the compare method with c2 passed as the argument (self refers to c1).

Inside compare, it checks if self.age (i.e., c1.age) is equal to c2.age. Since both are 28, the condition is True.

4.Conditional Statement:

The if condition evaluates to True, so the print("They are same") statement is executed.''')