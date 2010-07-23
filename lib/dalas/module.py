from sqlobject import *

class Module:
	def __init__(self, name, path, db, pipeline):
		self.name = name
		self.path = path
		self.db = db
		self.pipeline = pipeline
		self.open()

	def read(self):
		while True:
			line = self.file.readline()
			if line:
				self.process(line.strip())
			else:
				break

	def process(self, line):
		print line

	def open(self):
		self.file = open(self.path, "r")
		self.file.seek(0, 2)
		
	def close(self):
		self.file.close()

	def connect_db(self):
		return connectionForURI(self.db)