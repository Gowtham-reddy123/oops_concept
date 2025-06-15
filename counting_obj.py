class Counter():
	count=0
	def __init__(self):
		Counter.count+=1
a=Counter()
a=Counter()
a=Counter()
a=Counter()
a=Counter()
a=Counter()
a=Counter()
a=Counter()
a=Counter()
a=Counter()
a=Counter()
a=Counter()
print("Total objects created is : ",Counter.count)
a = Counter()
print(a.__dict__)            
print(Counter.__dict__['count']) 

