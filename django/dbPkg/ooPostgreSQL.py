# -*- coding: utf-8 -*-
# ooPostgreSQL from dbPkg Python Class v0.1-20090927
# Copyright (c) 2009 - Reinaldo de Carvalho <reinaldoc@gmail.com>

import psycopg2 as pg
import ooGeneric

class ooPostgreSQL(ooGeneric.ooGeneric):
	def __init__(self, host, user, password, database=""):
		ooGeneric.ooGeneric.__init__(self)
		self._dbHost = host
		self._dbUser = user
		self._dbPass = password
		self._db = database
		self._connect()

	def _connect(self):
		dsn = ('dbname=%s host=%s user=%s password=%s') % (database, host, user, password)
		self._dbHandle = pg.connect(dsn)
		self.queryHandle = self.dbHandle.cursor()
	
	def __del__(self):
		self._dbHandle.close()

	def insert(self, data):
		try:
			self._insert(self._queryHandle.execute, data)
			self._dbHandle.commit()
			return True
		except:
			return False
