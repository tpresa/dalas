# -*- coding: utf-8 -*-
# libRawLog plugin from logPkg Python Class v0.1-20090927
# Copyright (c) 2009 - Reinaldo de Carvalho <reinaldoc@gmail.com>

class RawLog:
	def __init__(self):
		pass
	
	def __del__(self):
		pass

	def insert(self, dbHandle, data):
		dbHandle.insert("INSERT INTO RawLog (rawdata) VALUES ('%s')" % data)
		return True
