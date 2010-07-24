from dalas.log import Log

class HttpLog(Log):
	def process(self, line):
		self.module.db.logs.insert({ "log": line })