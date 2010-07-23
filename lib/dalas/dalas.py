import time
from config import *

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
		try:
		    while True:
				for log in self.logs:
					log.read()
				time.sleep(1)
		except KeyboardInterrupt:
		    pass
		
		for log in self.logs:
			log.close()