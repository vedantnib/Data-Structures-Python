class node:
	def __init__(self,data):
		self.data=data
		self.next=None
class linkedlist:
	def __init__(self):
		self.head=None
	def printlist(self):
		current=self.head
		while(current is not None):
			print(current.data, end=" ")
			current=current.next
		print()
	def isempty(self):
		if self.head is None:
			return True
		else:
			return False
	def leng(self):
		current=self.head
		count=0
		while current:
			count+=1
			current=current.next
		return count
	def addbeg(self,newnode):
		nbeg=node(newnode)
		nbeg.next=self.head
		self.head=nbeg

	def addend(self,newnode):
		nn=node(newnode)
		current=self.head
		while current.next is not None:
			current=current.next
		current.next=nn
	def addpos(self,newnode,p):
		if p==0:
			self.addbeg(newnode)
		if p==self.leng():
			self.addend(newnode)
		else:
			prev=self.head
			nex=self.head.next
			for i in range(p-2):
				prev=prev.next
				nex=nex.next
			nn=node(newnode)
			prev.next=nn
			nn.next=nex

	def deletebeg(self):
		dele=self.head
		self.head=self.head.next
		dele=None
	def deleteend(self):
		if self.head is None:
			print("List is empty")
		dele1=self.head
		dele2=self.head.next
		while(dele2.next is not None):
			dele1=dele1.next
			dele2=dele2.next
		dele1.next=None
		dele2=None
	def deletepos(self,p):
		if p==0 or p==1:
			self.deletebeg()
		if p==self.leng():
			self.deleteend()
		curr=self.head
		currnex=self.head.next
		for i in range(p-2):
			curr=curr.next
			currnex=currnex.next
		curr.next=currnex.next
		currnex=None
	def deletevalue(self,val):
		curr=self.head
		currnex=self.head.next
		while(currnex.next is not None):
			if currnex.data==val:
				curr.next=currnex.next
				currnex=None
				return
			else:
				curr=curr.next
				currnex=currnex.next
		print("Element not found")
		return
	def findval(self,val):






ll=linkedlist()
while(1):
	print("Plan of action:")
	print("1.Insert node at beg")
	print("2.Insert node at end")
	print("3.Insert node at position p")
	print("4.Delete node at beg")
	print("5.Delete node at end")
	print("6.Delete node at position p")
	print("7.Delete by value")
	print("8.Print list")

	choice=input()
	if choice=="1":
		if ll.isempty():
			ll.head=node(int(input()))
		else:
			newnode=int(input())
			ll.addbeg(newnode)
	if  choice=="2":
		if ll.isempty():
			ll.head=node(int(input()))
		else:
			newnode=int(input())
			ll.addend(newnode)
	if choice=="3":
		if ll.isempty():
			ll.head=node(int(input()))
		else:
			p=int(input("Enter position of insertion: "))
			newnode=int(input())
			ll.addpos(newnode,p)
	if choice=="4":
		if ll.isempty():
			print("Linked list empty")
		else:
			ll.deletebeg()
	if choice=="5":
		if ll.isempty():
			print("Linked list empty")
		else:
			ll.deleteend()
	if choice=="6":
		if ll.isempty():
			print("Linked list empty")
		else:
			p=int(input("Enter position of deletion: "))

			ll.deletepos(p)
	if choice=="8":
		ll.printlist()
	if choice=="7":
		if ll.isempty():
			print("Linked list empty")
		else:
			val=int(input("Enter node value to be deleted: "))

			ll.deletevalue(val)

	if choice=="n":
		break
