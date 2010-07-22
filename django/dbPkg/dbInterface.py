# -*- coding: utf-8 -*-
# dbPkg Python Package v0.1-20090927
# Copyright (c) 2009 - Reinaldo de Carvalho <reinaldoc@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.

import re

class CANT_PARSE_BACKEND(Exception):
	pass

class DATABASE_ALREADY_SET(Exception):
	pass

class INVALID_CONNECTION_CONFIGURATION(Exception):
	pass

class dbInterface:
	re_url = re.compile(r'^(mysql|pgsql)://(.+?):(.+?)@(.+?):?(\d{0,5})?/(.*)$', re.I)
	dbPorts = { "mysql": 3306, "pgsql": 5432}
	
	def __init__(self):
		self.dbHandle = ""
		self.dbDict = {}

	def _setBackend(self, backend):
		try:
			match = dbInterface.re_url.match(backend)
			if not match:
				raise Exception
			self.dbDict["DbDriver"] = match.group(1)
			self.dbDict["Username"] = match.group(2)
			self.dbDict["Password"] = match.group(3)
			self.dbDict["Hostname"] = match.group(4)
			if match.group(5) and type(match.group(5)) == type(0):
				self.dbDict["Port"] = int(match.group(5))
			else:
				self.dbDict["Port"] = dbInterface.dbPorts.get(match.group(1))
				self.dbDict["Database"] = match.group(5)
			if match.group(6):
				self.dbDict["Database"] = match.group(6)
		except:
			raise CANT_PARSE_BACKEND

	def setBackend(self, backend):
		if self.dbDict:
			raise DATABASE_ALREADY_SET
		self._setBackend(backend)
		if self.dbDict.get("DbDriver").lower() == "mysql":
			from ooMySQL import ooMySQL
			self.dbHandle = ooMySQL(self.dbDict.get("Hostname"), self.dbDict.get("Username"), self.dbDict.get("Password"), self.dbDict.get("Database"))
		elif self.dbDict.get("DbDriver").lower() == "pgsql":
			from ooPostgreSQL import ooPostgreSQL
			self.dbHandle = ooPostgreSQL(self.dbDict.get("Hostname"), self.dbDict.get("Username"), self.dbDict.get("Password"), self.dbDict.get("Database"))
		elif self.dbDict.get("DbDriver").lower() == "sqlite":
			from ooSQLite import ooSQLite

	def insert(self, data):
		if self.dbHandle.insert(data):
			return True
		else:
			return False




