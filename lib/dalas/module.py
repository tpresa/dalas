from sqlobject import *
import time
import fcntl
import os

class Module:
	def __init__(self, parameters):
		self.parameters = parameters
		self.pipeline = self.create_pipeline()
		self.load_schema(self.connect_db())

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
			if not (pipe.process(line)):
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
		return connectionForURI(self.parameters["database"])
	
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
