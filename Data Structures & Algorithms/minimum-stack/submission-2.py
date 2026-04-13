class MinStack:
	def __init__(self):
		self.stack = []
		self.min_stack = []
	
	def push(self, val):
		self.stack.append(val)

		if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
			self.min_stack.append(val)
	
	def pop(self):
		if len(self.stack) > 0:
			popped = self.stack.pop()

			if self.min_stack[-1] == popped:
			    self.min_stack.pop()
	
	def top(self):
		if len(self.stack) > 0:
			return self.stack[-1]
		
	
	def getMin(self):
		if len(self.min_stack) > 0:
			return self.min_stack[-1]
        