import time, os, signal
from config import *
from logreads import ReadLogs

# Main application class
class Dalas:
	def __init__(self):
		self.quit   = False
		self.config = config()
		#FIXME: actually this is a list of modules
		# logs is an awful name
		self.logs   = []
		self.__connect_signals()
		self.__write_pid()

	def run(self):
		print time.strftime("%Y-%m-%d %X: STARTED", time.gmtime())
		
		for name in self.config["logs"]:
			modConfig = self.config["logs"][name]
			
			# Load a specifique module
			module = __import__("dalas.%s" % modConfig["module"].lower())
			module = getattr(module, "%s" % modConfig["module"].lower())
			module = getattr(module, modConfig["module"])

			log = module(name, modConfig)
			self.logs.append(log)

		self.read_loop()
		
		if os.path.exists(self.config["args"]["-p"]):
			os.unlink(self.config["args"]["-p"])

	# Loop in logs analyser
	def read_loop(self):
		
		self.rl = ReadLogs(self)
		
		try:
			for log in self.logs:
				self.rl.append(log)
			self.rl.read()
		except KeyboardInterrupt:
			pass
		
		self.rl.close()
	
	def __write_pid(self):
		f = open(self.config["args"]["-p"],'w+')
		print >> f, os.getpid()
		f.close()

	def __reopen_all_files(self, signum, frame):
		print time.strftime("%Y-%m-%d %X: RELOADED", time.gmtime())
		self.rl.reload()

	def __connect_signals(self):
		# Kill connect
		signal.signal(signal.SIGTERM, self.__quit)
		
		# Handles the SIGHUP
		# Logrotate will SIGHUP is when it runs
		# So that we must open our log files again
		signal.signal(signal.SIGHUP, self.__reopen_all_files)

	def __quit(self, signum, frame):
		print time.strftime("%Y-%m-%d %X: STOPED", time.gmtime())
		self.quit = True