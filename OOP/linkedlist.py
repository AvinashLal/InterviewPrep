class node(object):
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def __str__(self):
		return str(self.value)

class linkedlist(object):
	def __init__(self, node):
		self.head = node
		self.tail = node

	def add_node(self, new_node):
		self.tail.next = new_node
		self.tail = new_node

	def find_value(self, target):
		self.curr = self.head
		while self.curr:
			if self.curr.value == target:
				return True
			else:
				self.curr = self.curr.next 
		return False

	def __str__(self):
		self.curr = self.head
		output = ''
		while self.curr:
			output += str(self.curr) + ' '
			self.curr = self.curr.next 
		return output