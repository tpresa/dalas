# -*- coding: utf-8 -*-
# parseConfig from configPkg Python Class v0.1-20090927
# Copyright (c) 2009 - Reinaldo de Carvalho <reinaldoc@gmail.com>

import re

class CANT_READ_CONFIGURATION(Exception):
	pass

class NO_ENTRY_FOUND_IN_CONFIGURATION(Exception):
	pass

class parseBracketStyle:
	def __init__(self):
		self.ConfigDict = {}

	def __parseConfig(self, configData):
		re_config = re.compile(r'(\[.*\]\n(.*\n)*?(\n|$))')
		match = re_config.findall(configData)
		for entry in match:
			self.__parseEntries(entry[0])

	def __parseEntries(self, entry):
		entryName = ""
		for option in entry.split("\n"):
			if option:
				match = re.search("^\[(.*)\]", option)
				if match:
					entryName = match.group(1)
					self.ConfigDict[entryName] = {}
				else:
					optionList = option.split(" ", 1)
					self.ConfigDict[entryName][optionList[0].strip()] = optionList[1].strip()

	def parseConfig(self, path):
		try:
			fileHandle = open(path, "r")
			config = fileHandle.read()
			fileHandle.close()
		except IOError, e:
			raise CANT_READ_CONFIGURATION(e)
		self.__parseConfig(config)
		return self.ConfigDict
