from sqlobject import *

class Message(SQLObject):
	subject = StringCol()
	sender = StringCol()
	start = DateTimeCol()
	end = DateTimeCol()
	average = DateTimeCol()
	size = IntCol()
	checkin = DateTimeCol()
	done = BoolCol()	
	

class Recipient(SQLObject):
	label = StringCol()
	email_to = StringCol()
	orig_to = StringCol()
	relay_info = StringCol()
	delays = StringCol()
	dsn = StringCol()
	status = StringCol()
	queue = ForeignKey()
	checkin = DateTimeCol()

class Reject(SQLObject):
	label = StringCol()
	ident = RelatedJoin('MsgId')
	checkin = DateTimeCol()

class MsgId(SQLObject):
	label = StringCol()
	msgid = StringCol()
	msg = ForeignKey()
	queue = RelatedJoin('Queue')
	checkin = DateTimeCol()

class Event(SQLObject):
	label = StringCol()
	raw_month = StringCol()
	raw_day = StringCol()
	raw_time = StringCol()
	raw_hostname = StringCol()
	raw_actor = StringCol()
	raw_actor_cmd = StringCol()
	raw_pid = StringCol()
	raw_line = StringCol()
	queue = RelatedJoin('Queue')
	checkin = DateTimeCol()

class Queue(SQLObject):
	ident = StringCol()
	label = StringCol()
	done = BoolCol()

def load_schema(connect):
	tables = [Message]
	for table in tables:
		table._connection = connect
		table.createTable(ifNotExists=True)
