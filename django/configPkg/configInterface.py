# -*- coding: utf-8 -*-
# configPkg Python Package v0.1-20090927
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

from parseConfig import parseBracketStyle

class ENTRYNAME_DONT_HAVE_LOGIFLE_PATH(Exception):
	pass

class ENTRYNAME_DONT_HAVE_BACKEND(Exception):
	pass

class ENTRYNAME_DONT_HAVE_DATABASE(Exception):
	pass

class ENTRYNAME_DONT_HAVE_LOGPROCESSOR(Exception):
	pass

class NO_ENTRY_FOUND_IN_CONFIGURATION(Exception):
	pass

class NO_LOGFILES_FOUND_IN_CONFIGURATION(Exception):
	pass

class configInterface:
	def __init__(self, path):
		self.ConfigDict = {}
		self.__path = None
		self.__loadConfig(path)

	def __verify_config(self):
		if not self.ConfigDict:
			raise NO_ENTRY_FOUND_IN_CONFIGURATION
		if not self.getEntryNamesOfLogfiles():
			raise NO_LOGFILES_FOUND_IN_CONFIGURATION
		for logfileEntryName in self.getEntryNamesOfLogfiles():
			self.getPathByName(logfileEntryName)
			database = self.getDatabaseByName(logfileEntryName)
			self.getBackendByName(database)
			self.getLogProcessorByName(database)

	def __loadConfig(self, path):
		parse = parseBracketStyle()
		self.ConfigDict = parse.parseConfig(path)
		self.__verify_config()
		self.__path = path

	def reloadConfig(self, path=None):
		if path is None:
			path = self.path
		self.__loadConfig(path)

	def getPath(self):
		return self.__path

	def getEntry(self, name):
		return self.ConfigDict.get(name)

	def getEntryNames(self):
		return self.ConfigDict.keys()

	def getEntryNamesOfDatabases(self):
		databasesEntries = []
		for name in self.ConfigDict.keys():
			if self.ConfigDict.get(name).get('EntryType') == 'database':
				databasesEntries.append(name)
		return databasesEntries

	def getEntryNamesOfLogfiles(self):
		entries = []
		for name in self.ConfigDict.keys():
			if self.ConfigDict.get(name).get('EntryType') == 'logfile':
				entries.append(name)
		return entries

	def getLogfiles(self):
		entries = []
		for name in self.ConfigDict.keys():
			if self.ConfigDict.get(name).get('EntryType') == 'logfile':
				entries.append(self.ConfigDict.get(name).get('Path'))
		return entries
	
	def getPathByName(self, name):
		entry = self.ConfigDict.get(name)
		if entry:
			if entry.get('Path'):
				return entry.get('Path')
		raise ENTRYNAME_DONT_HAVE_LOGIFLE_PATH(name)

	def getBackendByName(self, name):
		entry = self.ConfigDict.get(name)
		if entry:
			if entry.get('Backend'):
				return entry.get('Backend')
		raise ENTRYNAME_DONT_HAVE_BACKEND(name)

	def getDatabaseByName(self, name):
		entry = self.ConfigDict.get(name)
		if entry:
			if entry.get('Database'):
				return entry.get('Database')
		raise ENTRYNAME_DONT_HAVE_DATABASE(name)

	def getLogProcessorByName(self, name):
		entry = self.ConfigDict.get(name)
		if entry:
			if entry.get('LogProcessor'):
				return entry.get('LogProcessor').split(" ")
		raise ENTRYNAME_DONT_HAVE_LOGPROCESSOR(name)
