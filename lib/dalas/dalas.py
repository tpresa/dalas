from config import *

class Dalas:
	def __init__(self):
		self.config = config()
	
	def run(self):
		print self.config["logs"]
		print self.config["args"]