class Student:
    school_name = "Naryana" 
    def __init__(self, name):
        self.name = name

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.school_name)  
print(s2.school_name)
  
Student.school_name = "Sri chaitanya"  

print(s1.school_name)  
print(s2.school_name)  
