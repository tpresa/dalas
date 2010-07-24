import sys

class Log:
	def __init__(self, module):
		self.module = module
	
	def process(self, line):
		# sys.stdout.write(line)
		return (True, None)
