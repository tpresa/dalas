# -*- coding: utf-8 -*-
# libTemplate plugin from logPkg Python Class v0.1-20090927
# Copyright (c) 2009 - Reinaldo de Carvalho <reinaldoc@gmail.com>

class TemplateLog:
	def __init__(self):
		pass
	
	def __del__(self):
		pass

	def _match2dict(self, match):
		if hasattr(match, "groupindex"):
			return match.groupindex()
		else:
			return match.groupdict()

	def _prepareSQL(self, dict, keylistOfBool=[]):
		for key in dict.keys():
			if key in keylistOfBool:
				if dict.get(key):
					dict[key] = "TRUE"
				else:
					dict[key] = "FALSE"
			elif dict.get(key):
				dict[key] = "'%s'" % dict.get(key)
			else:
				dict[key] = "NULL"
		return dict

	def insert(self, database, data):
		return True
