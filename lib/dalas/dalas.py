import time
from config import *
from logreads import ReadLogs

# Main application class
class Dalas:
	def __init__(self):
		self.config = config()
		self.logs   = []

	def run(self):
		for name in self.config["logs"]:
			modConfig = self.config["logs"][name]
			
			# Load a specifique module
			module = __import__("dalas.%s" % modConfig["module"].lower())
			module = getattr(module, "%s" % modConfig["module"].lower())
			module = getattr(module, modConfig["module"])

			log = module(modConfig)
			self.logs.append(log)

		self.read_loop()

	# Loop in logs analyser
	def read_loop(self):
		
		rl = ReadLogs()
		
		try:
			for log in self.logs:
				rl.append(log)
			rl.read()
		except KeyboardInterrupt:
			pass
		
		rl.close()
