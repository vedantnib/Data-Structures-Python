class node:
	def __init__(self,data):
		self.data=data
		self.next=None
		self.prev=None
class linkedlist:
	def __init__(self):
		self.head=None
		self.tail=None
	def isempty(self):
		if self.head is None:
			return True
		else: return False
	def leng(self):
		current=self.head
		count=0
		while(current is not None):
			count+=1
			current=current.next
		print(count)
	def insertbeg(self,data):
		if self.isempty():
			nn=node(data)
			nn.prev=None
			self.head=nn
			self.tail=nn
		else:
			nn=node(data)
			nn.prev=None
			nn.next=self.head
			self.head.prev=nn
			self.head=nn
	def insertend(self,data):
		nn=node(data)
		if self.isempty():
			self.head=nn
			self.tail=nn
		else:
			self.tail.next=nn
			nn.prev=self.tail
			nn.next=None
			self.tail=nn
	def insertpos(self,data,p):
		nn=node(data)
		if self.isempty() or p==0:
			self.head=nn
			self.tail=nn
		else:
			current=self.head
			for i in range(p-2):
				current=current.next
			nn.next=current.next
			current.next.prev=nn
			current.next=nn
			nn.prev=current
	def deletebeg(self):
		self.head=self.head.next
		self.head.prev=None
	def deleteend(self):
		self.tail=self.tail.prev
		self.tail.next=None
	def deletepos(self,pos):
		current=self.head
		for i in range(pos-1):
			current=current.next
		current.prev.next=current.next
		current.next.prev=current.prev
		current=None


	def printlist(self):
		current=self.head
		while(current is not None):
			print(current.data,end=" ")
			current=current.next
		print()
dl=linkedlist()
dl.insertbeg(20)
dl.printlist()
dl.insertbeg(400)
dl.printlist()
dl.insertend(500)
dl.printlist()
dl.insertend(67)
dl.printlist()
dl.insertbeg(88)
dl.printlist()
dl.printlist()
dl.insertpos(38,3)
dl.printlist()
dl.deletebeg()
dl.printlist()
dl.deleteend()
dl.printlist()
dl.deletepos(3)
dl.printlist()
#dl.leng()