from dalas.module import Module
import schema

class Mail(Module):
	def __init__(self, name, path, db, pipeline):
		Module.__init__(self, name, path, db, pipeline)
		schema.load_schema(self.connect_db())