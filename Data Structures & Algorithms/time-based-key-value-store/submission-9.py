class TimeMap:
	def __init__(self):
		self.store = defaultdict(list)
	
	def set(self, key, value, timestamp):
		self.store[key].append([value, timestamp])
		
	def get(self, key, timestamp):
		result = ""
		l = 0
		r = len(self.store[key]) - 1
		
		while l <= r:
			m = (l + r) // 2
			
			if self.store[key][m][1] <= timestamp:
				result = self.store[key][m][0]
				l = m + 1
			else:
				r = m - 1
		
		return result
        
