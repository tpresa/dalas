from dalas.module import Module
import schema

class Mail(Module):
	def load_schema(self, db):
		return schema.load_schema(db)