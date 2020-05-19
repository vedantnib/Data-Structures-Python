class node:
	def __init__(self,data):
		self.data=data
		self.next=None
class stack:
	def __init__(self):
		self.head=None
	def isempty(self):
		if self.head is None:
			return True
		else:
			return False
	def printstack(self):
		current=self.head
		while(current is not None):
			print(current.data)
			current=current.next

	def leng(self):
		current=self.head
		count=0
		while current:
			count+=1
			current=current.next
	def push(self,newnode):
		nbeg=node(newnode)
		nbeg.next=self.head
		self.head=nbeg
	def pop(self):
		dele=self.head
		ele=self.head.data
		self.head=self.head.next
		dele=None
		return ele
st=stack()
while(1):
	print("Plan of action:")
	print("1.Push node")
	print("2.Pop node")
	print("3.Print stack")

	choice=input()
	if choice=="1":
		if ll.isempty():
			ll.head=node(int(input()))
		else:
			newnode=int(input())
			ll.push(newnode)
	if choice=="2":
		if ll.isempty():
			print("Stack empty")
		else:
			popped=ll.deletebeg()
			print("popped element: "+popped)
	if choice=="3":
		ll.printstack()
	if choice=="n":
		break
