class node:
	def __init__(self,data):
		self.data=data
		self.next=None
class circular_list:
	def __init__(self):
		self.last=None
	def isempty(self):
		if self.last is None:
			return True
		else: return False

	def printlist(self):
		current=self.last.next
		while(current):
			print(current.data,end=" ")
			current=current.next
			if current==self.last.next:
				break
		print()
	def insertbeg(self,data):
		nn=node(data)
		if self.isempty():
			self.last=nn
			self.last.next=nn
		else:
			nn.next=self.last.next
			self.last.next=nn
	def insertend(self,data):
		nn=node(data)
		if self.isempty():
			self.last=nn
		else:
			nn.next=self.last.next
			self.last.next=nn
			self.last=nn
	def insertpos(self,data,p):
		nn=node(data)
		current=self.last.next
		for i in range(p-2):
			current=current.next
		nn.next=current.next
		current.next=nn
	def deletebeg(self):
		del1=self.last.next
		self.last.next=del1.next
		del1=None
	def deleteend(self):
		current=self.last.next
		del1=self.last
		while(current):
			current=current.next
			if current.next==self.last:
				break
		current.next=del1.next
		self.last=current
		del1=None
	def deletepos(self,p):
		current=self.last.next
		current2=self.last.next.next
		for i in range(p-2):
			current=current.next
			current2=current2.next
		current.next=current2.next
		current2=None




#	def leng(self):

cl=circular_list()
cl.insertbeg(20)
cl.insertbeg(40)
cl.insertbeg(70)
cl.insertend(99)
cl.insertend(240)
cl.insertend(22)

cl.printlist()
cl.deleteend()
cl.printlist()
cl.deletebeg()
cl.printlist()
cl.deletepos(3)
cl.printlist()