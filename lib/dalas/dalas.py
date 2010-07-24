import time, os, signal
from config import *
from logreads import ReadLogs

# Main application class
class Dalas:
	def __init__(self):
		self.config = config()
		#FIXME: actually this is a list of modules
		# logs is an awful name
		self.logs   = []
		self.__write_pid()
		self.__connect_signals()

	def run(self):
		for name in self.config["logs"]:
			modConfig = self.config["logs"][name]
			
			# Load a specifique module
			module = __import__("dalas.%s" % modConfig["module"].lower())
			module = getattr(module, "%s" % modConfig["module"].lower())
			module = getattr(module, modConfig["module"])

			log = module(name, modConfig)
			self.logs.append(log)

		self.read_loop()

	def reopen_all_files(self, signum, frame):
		print "Reload..."
		# for log in self.logs:
		# 	log.reopen_log()

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
	
	def __write_pid(self):
		f = open(self.config["args"]["-p"],'w+')
		print >> f, os.getpid()
		f.close()
		
	def __connect_signals(self):
		# Handles the SIGHUP
		# Logrotate will SIGHUP is when it runs
		# So that we must open our log files again
		signal.signal(signal.SIGHUP, self.reopen_all_files)