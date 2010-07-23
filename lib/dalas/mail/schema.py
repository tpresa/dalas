from sqlobject import *

class Message(SQLObject):
	subject = StringCol()
	
def load_schema(connect):
	Message._connection = connect
	Message.createTable(ifNotExists=True)