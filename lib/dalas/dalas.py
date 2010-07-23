import select
from config import *

class Dalas:
	def __init__(self):
		self.config = config()
		self.logs   = []

	def run(self):
		for name in self.config["logs"]:
			modConfig = self.config["logs"][name]
			
			module = __import__("dalas.%s" % modConfig["module"])
			module = getattr(module, "%s" % modConfig["module"])
			module = getattr(module, modConfig["module"].title())
		
			log = module(name, modConfig["path"], modConfig["database"], modConfig["pipeline"])
			self.logs.append(log)