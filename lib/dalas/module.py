import time
import fcntl
import os
import pymongo

class Module:
	def __init__(self, name, parameters):
		self.name = name
		self.parameters = parameters
		self.pipeline = self.create_pipeline()
		self.db = self.connect_db()

	# Read lines in file description
	def read(self):
		while True:
			line = self.file.readline()
			if line:
				self.process(line)
			else:
				break

	def process(self, line):
		for pipe in self.pipeline:
			cont, data = pipe.process(line)
			if data != None:
				self.ev_manager.HandleEvent(line, data)
			if not (cont):
				break

	# Open file description
	def open(self):
		fd = file(self.parameters["path"], "r")
		fd.seek(0,2)
		return fd

	# Close file description
	def close(self):
		return self.file.close()

	# Connection to database
	def connect_db(self):
		conn = pymongo.Connection(self.parameters["database"]["host"], self.parameters["database"]["port"])
		return conn[self.name]

	# Create a pipeline objects
	def create_pipeline(self):
		pipes = []
		for pipe in self.parameters["pipeline"]:
			# Load a specifique module
			module = __import__("dalas.%s.%s" % (self.parameters["module"].lower(), pipe.lower()))
			module = getattr(module, "%s" % self.parameters["module"].lower())
			module = getattr(module, "%s" % pipe.lower())
			module = getattr(module, pipe)
			pipes.append(module(self))
		return pipes
