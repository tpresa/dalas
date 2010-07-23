from pyparsing import *
import calendar

class DalasParser:

	# Grammar
	#FIXME Check these rules
	MONTH = oneOf(list(calendar.month_abbr)[1:])
	DAY = Regex("0[1-9]|1[0..9]|2[0-9]|3[01]")
	TIME = Regex("([0-1][0-9]|2[01234]):[0-5][0-9]:[0-5][0-9]")
	HOSTNAME = Word(printables)
	PROCESSNAME = Regex("postfix")
	CHILDPROCESS = Regex("virtual|cleanup|smtp")
	PFPID = Word(nums)
	QUEUEID = Word(alphanums)
	EMAIL = Regex("[^>]*")
	MESSAGEID = Regex("[^>]*")
	RELAY = Regex("[^,]*")
	DELAY = Regex("[^,]*")
	DSN = Regex("[^,]*")
	DELAYS = Regex("[^,]*")
	STATUS = Regex("deferred|sent|bounced")
	STATUSMSG = Regex(".*")
	
	CLEANUP = Group(Suppress('message-id=<') + MESSAGEID + Suppress('>'))
	VIRTUAL = Group(Suppress('to=<') + EMAIL + Suppress('>,') + Suppress('relay=') + RELAY + Suppress(',') + Suppress('delay=') + DELAY + Suppress(',') + Suppress('status=') + STATUS + STATUSMSG)
	SMTP = Group(Suppress('to=<') + EMAIL + Suppress('>,') + Suppress('orig_to=<') + EMAIL + Suppress('>,') + Suppress('relay=') + RELAY + Suppress(',') + Suppress('delay=') + DELAY + Suppress(',') + Suppress('delays=') + DELAYS + Suppress(',') + Suppress('dsn=') + DSN + Suppress(',') + Suppress('status=') + STATUS + STATUSMSG)
	
	LOGLINE = Group(MONTH + DAY + TIME + HOSTNAME + PROCESSNAME + Suppress('/') + CHILDPROCESS + Suppress('[') + PFPID + Suppress(']') + Suppress(':') + QUEUEID + Suppress(':') + Or([VIRTUAL, SMTP, CLEANUP]))
	
	def __init__(self, input):
		self.input = input

	def getLine(self):
		return open(self.input, 'r').readlines()

	def parse(self):
		results = []
		for line in self.getLine():
			try:
				parsed = self.LOGLINE.parseString(line)[0]
			except:
				pass
			else:
				results.append({
					'unique' : parsed[7], #FIXME Choose a better unique identifier
					'month' : parsed[0],
					'day' : parsed[1],
		  	  'time' : parsed[2],
					'hostname' : parsed[3],
		  	  'process' : parsed[4],
		  	  'childprocess' : parsed[5],
					'pid' : parsed[6],
					'queueId' : parsed[7],
		  	  'output' : self.formatResult(parsed[5], parsed[8])
				})
		return results

	def formatResult(self, actor, output):
		if actor == 'smtp':
			return { 'to' : output[0],
							 'orig_to' : output[1],
							 'relay' : output[2], 
							 'delay' : output[3],
							 'delays' : output[4],
							 'dsn' : output[5],
							 'status' : output[6], 
							 'description' : output[7].lstrip('(').rstrip(')') }
		if actor == 'virtual':
			return { 'to' : output[0], 
							 'relay' : output[1], 
							 'delay' : output[2], 
							 'status' : output[3], 
							 'description' : output[4].lstrip('(').rstrip(')') }
		if actor ==	'cleanup':
			return { 'message-id' : output[0] }
		else:
			return False

# Sample usage
print DalasParser('../input_data/postfix.log').parse()
