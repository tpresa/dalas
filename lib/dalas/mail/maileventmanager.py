from dalas.eventmanager import EventManager

class MailEventManager(EventManager):
	def __init__(self, module):
		self.module       = module
		self.db           = module.db
		self.QueueList    = { }
		self.QueueRawData = { }
		self.Queuestatus  = { }
		self.actor_cmd    = None
		self.cmd = {
			'smtp'   : self.Smtp,
			'nqmgr'  : self.Nqmgr,
			'qmgr'   : self.Qmgr,
			'cleanup': self.CleanUp,
			'pickup' : self.PickUp
		}

	def HandleEvent(self, line, data):
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
		self.db.events.insert(event)
		
		print "Save a event..."

		#Check if has actor... and execute...
		if data and self.cmd.has_key(data['childprocess']):
			self.cmd[data['childprocess']](data)
		else:
			#FIX-ME: Create handle to exceptions:
			#need regex to cover
			return False

	def Smtp(self, data):
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
		self.db.recipients.insert(recipient)
		
		print "Save a recipient..."

	def Nqmgr(self, data):
		pass

	def Qmgr(self, data):
		pass
	
	def CleanUp(self, data):
		pass

	def PickUp(self, data):
		pass