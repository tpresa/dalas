# -*- coding: utf-8 -*-
# logPkg Python Package v0.1-20090927
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

import dbPkg

class CANT_CONNECT_TO_BACKEND(Exception):
	pass

class CONFIGURATION_NOT_LOADED(Exception):
	pass

class logProcessor:
	def __init__(self):
		self.configObj = ""
		self.logProcessors = {}

	def __loadLogProcessor(self, processor):
		if self.logProcessors.get(processor):
			return True
		module = __import__("logPkg.lib%s" % processor)
		module = getattr(module, "lib%s" % processor)
		module = getattr(module, processor)
		self.logProcessors[processor] = module()

	def setConfig(self, configObj):
		self.configObj = configObj

	def initialize(self):
		if not self.configObj:
			raise CONFIGURATION_NOT_LOADED
		self.dbHandle = {}
		for dbEntry in self.configObj.getEntryNamesOfDatabases():
			try:
				self.dbHandle[dbEntry] = dbPkg.dbInterface()
				self.dbHandle[dbEntry].setBackend(self.configObj.getBackendByName(dbEntry))
			except Exception, e:
			    raise CANT_CONNECT_TO_BACKEND([self.configObj.getBackendByName(dbEntry), e])

	def insert(self, dbEntry, data):
		database = self.configObj.getDatabaseByName(dbEntry)
		logProcessors = self.configObj.getLogProcessorByName(database)
		for processor in logProcessors:
			self.__loadLogProcessor(processor)
			if self.logProcessors.get(processor).insert(self.dbHandle[database], data):
				break
