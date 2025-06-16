class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hi", self.name)

p = Person("Gowtham")
p.greet()
