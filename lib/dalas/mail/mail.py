from dalas.module import Module
from maileventmanager import *

class Mail(Module):
	def __init__(self, name, parameters):
		Module.__init__(self, name, parameters)
		self.ev_manager = MailEventManager(self)
