from pyparsing import *
import calendar

class DalasParser:

	# Grammar
	MONTH = oneOf(list(calendar.month_abbr)[1:])
	DAY = Regex("0[1-9]|1[0..9]|2[0-9]|3[01]")
	TIME = Regex("([0-1][0-9]|2[01234]):[0-5][0-9]:[0-5][0-9]")
	HOSTNAME = Word(printables)
	PROCESSNAME = Regex("postfix")
	CHILDPROCESS = Regex("virtual|cleanup|smtp")
	PFPID = Word(nums)
	QUEUEID = Word(alphanums)
	EMAIL = Regex("[^>]*") #FIXME Could be improved
	MESSAGEID = Regex("[^>]*") #FIXME Could be improved
	RELAY = Word(alphanums)
	DELAY = Word(alphanums)
	STATUS = Regex("deferred|sent|bounced")
	STATUSMSG = Regex(".*")
	
	CLEANUP = Group(Suppress('message-id=<') + MESSAGEID + Suppress('>'))
	VIRTUAL_OR_SMTP = Group(Suppress('to=<') + EMAIL + Suppress('>,') + Suppress('relay=') + RELAY + Suppress(',') + Suppress('delay=') + DELAY + Suppress(',') + Suppress('status=') + STATUS + STATUSMSG)
	
	LOGLINE = Group(MONTH + DAY + TIME + HOSTNAME + PROCESSNAME + Suppress('/') + CHILDPROCESS + Suppress('[') + PFPID + Suppress(']') + Suppress(':') + QUEUEID + Suppress(':') + Or([VIRTUAL_OR_SMTP, CLEANUP]))
	
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
		if actor == 'virtual' or actor == 'smtp':
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
