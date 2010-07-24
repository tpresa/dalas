from dalas.eventmanager import EventManager
import schema

class MailEventManager(EventManager):
	def __init__(self):
		self.QueueList    = { }
		self.QueueRawData = { }
		self.Queuestatus  = { }
		self.actor_cmd    = None
		self.cmd = {
			'nqmgr'  : self.Nqmgr,
			'qmgr'   : self.Qmgr,
			'smtp'   : self.Smtp,
			'cleanup': self.CleanUp,
			'pickup' : self.PickUp
		}
	
	def HandleEvent(self, data):
		
		#Check if has actor... and execute...
		if data and self.cmd.has_key(data['childprocess']):
			self.cmd[data['childprocess']](data, queue)
		else:
			#FIX-ME: Create handle to exceptions:
			#need regex to cover
			return False

	def CleanUp(self, data, queue):
		pass

	def PickUp(self, data, queue):
		print data