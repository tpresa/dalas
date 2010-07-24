from dalas.eventmanager import EventManager

class MailEventManager(EventManager):
	def __init__(self, module):
		self.module       	= module
		self.db		        = module.db
		self.UniqueQList	= { }
		self.QueueList    	= { }
		self.QueueRawData 	= { }
		self.Queuestatus  	= { }
		
		self.uniqueQs 		= self.db.uniqueQs		
		self.actor_cmd    = None
		self.cmd = {
			'smtp'   : self.Smtp,
			'nqmgr'  : self.Nqmgr,
			'qmgr'   : self.Qmgr,
			'cleanup': self.CleanUp,
			'pickup' : self.PickUp
		}

	def HandleEvent(self, line, data):
		#Check if queue exist in uniqueQ, if yes glue with event...
		queue_id  = { "label" : data["unique"] }
		
		if not (queue = self.uniqueQs.find_one(queue_id)):
			queue = self.uniqueQs.insert(queue_id)
		
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
		
		self.uniqueQs.update(queue_id, {"$push":{"events": event}},True)
		
		#Check if has actor... and execute...
		if data and self.cmd.has_key(data['childprocess']):
			self.cmd[data['childprocess']](data, queue)
		else: 
			#FIX-ME: Create handle to exceptions:
			#need regex to cover
			return False

	def Smtp(self, data, queue):
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
		
		self.uniqueQs.update(queue_id, {"$push":{"recipients": recipient}},True)
		

	def Nqmgr(self, data, queue):
		pass

	def Qmgr(self, data, queue):
		pass
	
	def CleanUp(self, data, queue):
		pass

	def PickUp(self, data, queue):
		pass
