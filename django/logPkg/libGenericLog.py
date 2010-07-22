# -*- coding: utf-8 -*-
# libGenericLog plugin from logPkg Python Class v0.1-20090927
# Copyright (c) 2009 - Reinaldo de Carvalho <reinaldoc@gmail.com>

import re
from libTemplate import TemplateLog

class GenericLog(TemplateLog):
	re_genericLog = re.compile(r"^([A-Za-z]{3} \d{1,2} {1,2}\d\d:\d\d:\d\d) (?P<hostname>.*?) (?P<process>.*?:) (?P<data>.*)$")

	def __init__(self):
		pass

	def __del__(self):
		pass

	def insert(self, dbHandle, data):
		try:
			match = GenericLog.re_genericLog.match(data)
			result = self._match2dict(match)
			result = self._prepareSQL(result)
			if dbHandle.insert("INSERT INTO GenericLog (date, hostname, process, data) VALUES (now(), %(hostname)s, %(process)s, %(data)s)" % result):
				return True
			else:
				return False
		except:
			return False
