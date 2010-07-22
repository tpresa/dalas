import yaml
import sys

class Config:
	def __init__(self):
		self.args = self.getProgramArgs()
		fp = file(self.args.get('-c'))
		if fp:
			self.conf = yaml.load(fp)
			fp.close
		else:
			print "Error in open configure file: %" % self.args.get('-c')

	def getProgramArgs(self):
		readArgs = {"-c": 1}
		lastArg = ""
		for arg in sys.argv[1:]:
			if readArgs.get(lastArg) == 2:
				readArgs[lastArg] = arg
			elif readArgs.get(lastArg) == 1:
				self.banner()
			lastArg = arg

			if arg == '-c' or arg == '--conf':
				readArgs['-c'] = 2
				lastArg = '-c'
			elif arg == '-v' or arg == '--version':
				self.version()

		if type(readArgs.get('-c')) == type(0):
			self.banner()
		return readArgs

	def banner(self):
		print """
		Usage: %s -c configFile
Options available:
    -c ,    --conf            Path to the configuration file
    -h ,    --help            Show this help
    -v ,    --version         Print program version

Bugs: <reinaldoc@gmail.com>.
		""".strip() % sys.argv[0]
		sys.exit(1)

	def version(self):
		print __version__
		sys.exit(0)