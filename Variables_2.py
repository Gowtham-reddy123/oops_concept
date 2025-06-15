class Student:
	Institute="SGC"
	def __init__(self,name):
		self.name=name
s1=Student("Gowtham")
s2=Student("Karthik")
s1.Institute="TALLY EDUCATION PVLTD "
Student.Institute="SRI GOODWILL COMPUTERS"
print(s1.name,s1.Institute)
print(s2.name,s2.Institute)