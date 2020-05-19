class stack:
	def __init__(self, limit=10):
		self.stax=limit*[]
		self.limit=limit
		self.top=-1
	def isempty(self):
		if len(self.stax)==0:
			return True
		else:
			return False
	def isfull(self):
		if len(self.stax)>=self.limit:
			return True
		else:
			return False
	def push(self,data):
		if self.isfull():
			self.resize()
			self.stax.append(data)
		else:
			self.stax.append(data)
	def popele(self):
		if self.isempty():
			print("Stack Underflow")
		else:
			print(self.stax.pop())
	def size(self):
		return len(self.stax)
	def resize(self):
		if self.size()==self.limit:
			newstck=list(self.stax)
			self.limit=2*self.limit
			self.stax=newstck

	def printstack(self):
		if self.isempty():
			print("Stack empty")
		if self.isfull():
			print("Stack full")
		else:
			for i in range(len(self.stax)-1,-1,-1):
				print(self.stax[i],end=" ")
			print()


mystack=stack(10)
mystack.push(11)
mystack.push(22)
mystack.push(33)
mystack.push(44)
mystack.push(55)
mystack.push(66)
mystack.push(77)
mystack.push(88)
mystack.push(99)
mystack.push(100)
mystack.push(111)
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)
mystack.push(5)
mystack.push(6)
mystack.push(7)
mystack.push(8)
mystack.push(9)
mystack.push(11)
mystack.printstack()
for i in range(5):
	mystack.popele()
mystack.printstack()
for i in range(6):
	mystack.popele()
	#mystack.printstack()
print("Stack size: ",mystack.size())