import fcntl, os
from select import *
# import threading

class ReadLogs():
	kq   = None
	poll = None
	
	def __init__(self, dalas):
		self.dalas = dalas

		try:
			self.kq   = kqueue()
		except:
			self.poll = poll()
		
		self.logs = []
	
	def append(self, log):
		# Open file and go to end
		flog = file(log.parameters["path"], "r")
		flog.seek(0, 2)

		# Register files
		fd = flog.fileno()
		fl = fcntl.fcntl(fd, fcntl.F_GETFL)
		fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
		self.__register_file(fd)

		log.file = flog
		self.logs.append(log)
	
	# def read_lines(self):
	# 	while True:
	# 		if not log.read():
	# 			break
	# 	threading.current_thread().

	def read(self):
		while not self.dalas.quit :
			evts = self.__wait()
			if len(evts):
				for ev in evts:
					for log in self.logs:
						if log.file.fileno() == ev:
							log.read()
							break

	def reload(self):
		pass

	def close(self):
		self.__close()
		[log.file.close() for log in self.logs]
		
	def __wait(self):
		if self.kq:
			evts = self.kq.control([], 1, None)
				
			return [e.ident for e in evts]
		else:
			evts = self.poll.poll(1)
			return [e[0] for e in evts]

	def __close(self):
		if self.kq:
			return self.kq.close()
		else:
			[self.poll.unregister(log.file.fileno()) for log in self.logs]
			return self.poll.close()

	def __register_file(self, fd):
		if self.kq:
			ev = kevent(fd, KQ_FILTER_READ, KQ_EV_ADD | KQ_EV_ENABLE)
			return self.kq.control([ev], 0, 0)
		else:
			return self.poll.register(fd, POLLIN)