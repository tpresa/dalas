from dalas.eventmanager import EventManager

class MailEventManager(EventManager):
	def __init__(self, module):
		self.module = module
		self.db		= module.db
		
		self.messages   = self.db.messages
		self.actor_cmd  = None
		self.cmd = {
			'smtp'   : self.Smtp,
			'nqmgr'  : self.Nqmgr,
			'qmgr'   : self.Qmgr,
			'cleanup': self.CleanUp,
			'pickup' : self.PickUp
		}


	def HandleEvent(self, line, data):
		#Check if queue exist in uniqueQ, if yes glue with event...
		msg_id  = { "queue" : data["unique"], "status" : "open" }
		msg     = self.messages.find_one(msg_id)

		if not msg:
			msg = self.messages.insert(msg_id)
		else:
		    msg = msg["_id"]
		
		event  = {
			"label"     : data['label'],
			"raw_month" : data['month'],
			"raw_day"   : data['day'],
			"raw_time"  : data['time'],
			"raw_hostname"   : data['hostname'],
			"raw_actor_cmd " : data['childprocess'],
			"raw_actor" : data['process'],
			"raw_pid"   : data['pid'],
			"raw_line"  : line
		}
		
		self.messages.update({ "_id" : msg }, {"$push":{"events": event}},True)
		
		print "Insert a event in message"
		
		#Check if has actor... and execute...
		if data and self.cmd.has_key(data['childprocess']):
			self.cmd[data['childprocess']](data, msg)
		else: 
			#FIX-ME: Create handle to exceptions:
			#need regex to cover
			return False

	def Smtp(self, data, msg):
		# FIX-ME:
		output = data['output']
		
		recipient = {
			"queue"    : data['unique'],
			"label"    : 'send to: %s' % output['to'],
			"email_to" : output['to'],
			"orig_to " : output['orig_to'],
			"delays"   : output['delays'],
			"dsn"      : output['dsn'],
			"status"   : output['status'],
			"relay"    : output['relay']
		}
		
		#Do not insert if recipients exists, just update status...
		#
		self.messages.update({ "_id" : msg }, {"$push":{"recipients": recipient}},True)


	def Nqmgr(self, data, queue):
		#I dont know what i do.... : )
		pass

	def Qmgr(self, data, queue):
		# Just check if removed is true,  and close msg...
		# otherwise, update state label....
		print data,queue
	
	
	
	def CleanUp(self, data, msg):
		#make message human redeable...
		#receive From, and Subjects...
		#output = data['output']
		print data
		#self.messages.update({ "_id" : msg }, {"$push":{"recipients": recipient}},True)
		
		
		
		

	def PickUp(self, data, queue):
		print data,queue
