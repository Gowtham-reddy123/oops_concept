class Car:
	wheel=4#class variable
	def __init__(self):
		self.mil=10
		self.com="BMW"
c1=Car()
c2=Car()
c1.mil=8# we can change this because it is instance variable changes from object to object
print(c1.com,c1.mil,c1.wheel)
print(c2.com,c2.mil,c2.wheel)
Car.wheel=5#
print(c1.com,c1.mil,c1.wheel)
print(c2.com,c2.mil,c2.wheel)
