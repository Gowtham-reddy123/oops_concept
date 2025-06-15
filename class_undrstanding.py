class Laptop:
	brand="Macbookpro"

	def __init__(self,model):
		self.model=model# this is instance variable because it is created under and init method 
L1=Laptop("m3")
L2=Laptop("m4")
L1.brand="DELL"# converting or shadowing the instance variable for brand
Laptop.brand="Macbookpro"
print(L1.brand)
print(L2.brand)
print(L1.__dict__,L2.__dict__)