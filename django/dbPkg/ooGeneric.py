# -*- coding: utf-8 -*-
# ooGeneric from dbPkg Python Class v0.1-20090927
# Copyright (c) 2009 - Reinaldo de Carvalho <reinaldoc@gmail.com>

class ooGeneric:
	__reconnectDelayMax = 500
	__reconnectDelayIncrement = 10
	
	def __init__(self):
		self.__reconnectDelay = 0
		self.__reconnectCounter = 0
	
	def _insert(self, handle, data):
		try:
			handle(data.replace("'","\'"))
			self.__reconnectDelay = 0
		except:
			if self.__reconnectCounter == 0:
				if self.__reconnectDelay < ooGeneric.__reconnectDelayMax:
					self.__reconnectDelay += ooGeneric.__reconnectDelayIncrement
				self.__reconnectCounter = self.__reconnectDelay
				self._connect()
				handle(data.replace("'","\'"))
			else:
				self.__reconnectCounter -= 1
 
