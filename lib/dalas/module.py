from sqlobject import *

class Module:
	def __init__(self, name, path, db, pipeline):
		self.name = name
		self.path = path
		self.db = db
		self.pipeline = pipeline
	
	def connect_db(self):
		return connectionForURI(self.db)