# -*- coding: utf-8 -*-
# ooMySQL from dbPkg Python Class v0.1-20090927
# Copyright (c) 2009 - Reinaldo de Carvalho <reinaldoc@gmail.com>

import MySQLdb
import ooGeneric

class ooMySQL(ooGeneric.ooGeneric):
	def __init__(self, host, user, password, database=""):
		ooGeneric.ooGeneric.__init__(self)
		self._dbHost = host
		self._dbUser = user
		self._dbPass = password
		self._db = database
		#self._connect()
	
	def _connect(self):
		self._dbHandle = MySQLdb.connect(self._dbHost, self._dbUser, self._dbPass)
		if self._db:
			self._dbHandle.select_db(self._db)
		self._queryHandle = self._dbHandle.cursor()

	def __del__(self):
		self._dbHandle.close()

	def selectDb(self, database):
		self._dbHandle.select_db(database)

	def insert(self, data):
		try:
			self._insert(self._queryHandle.execute, data)
			return True
		except:
			return False
