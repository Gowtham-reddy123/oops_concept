class Computer:
	def __init__(self,cpu,ram):
		self.cpu=cpu
		self.ram=ram
	def config(self):
		print("config is ",self.cpu,self.ram)
com1=Computer('i5',16)
com2=Computer('Rygen 3',8)
com1.config()
com2.config()

print('''

		
	  Step 1: Python sees class Computer
Python defines the Computer class.

It now knows that it can create Computer objects with a cpu, ram, and a config() method.

 Step 2: com1 = Computer('i5', 16)
You are creating an object of the Computer class.

This automatically calls the special method __init__().

Inside __init__(self, cpu, ram):
self refers to the new object being created → com1

cpu = 'i5', ram = 16

com1.cpu = 'i5'
com1.ram = 16
Now com1 has:

cpu = 'i5'

ram = 16

 Step 3: com2 = Computer('Rygen 3', 8)
Same as above: creates another object, com2

Calls __init__() with cpu = 'Rygen 3', ram = 8

So:

python
Copy
Edit
com2.cpu = 'Rygen 3'
com2.ram = 8
Now you have two independent objects:

com1 = 'i5', 16

com2 = 'Rygen 3', 8

 Step 4: com1.config()
Calls the config() method for com1

Inside config(self), self refers to com1

So it prints:

config is i5 16
Step 5: com2.config()
Calls the config() method for com2

Inside config(self), self refers to com2

So it prints:

config is Rygen 3 8
Final Output:
config is i5 16
config is Rygen 3 8
 Key Concepts for Beginners:
Concept	Meaning
__init__ method	Special method that runs when an object is created (constructor)
self	Refers to the current object inside class methods
Instance Variables	self.cpu, self.ram are variables tied to each object
Method Call	com1.config() means “run the config method for com1


''')
		