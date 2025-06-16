class Student:
	school="Telusuko"
	def __init__(self,m1,m2,m3):
		self.m1=m1
		self.m2=m2
		self.m3=m3
	def avg(self):
		return (self.m1+self.m2+self.m3)/3
s1=Student(23,65,79)
s2=Student(90,21,45)
print(s1.avg())