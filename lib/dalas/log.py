class Log:
	def __init__(self, module):
		self.module = module
	
	def process(self, line):
		print line
		return True

        
