import yaml
import sys

# Prints the usage and exits
def usage():
	print """
Usage: %s -c configFile
Options available:
-c ,    --conf            Path to the configuration file
-h ,    --help            Show this help
-v ,    --version         Print program version

Bugs: <reinaldoc@gmail.com>.
	""".strip() % sys.argv[0]
	sys.exit(1)

# Print the version
def version():
	print DALAS_VERSION
	sys.exit(0)

def getProgramArgs():

	readArgs = {"-c": 1}
	lastArg = ""
	for arg in sys.argv[1:]:
		if readArgs.get(lastArg) == 2:
			readArgs[lastArg] = arg
		elif readArgs.get(lastArg) == 1:
			usage()
		lastArg = arg

		if arg == '-c' or arg == '--conf':
			readArgs['-c'] = 2
			lastArg = '-c'
		elif arg == '-v' or arg == '--version':
			version()

	if type(readArgs.get('-c')) == type(0):
		usage()
	return readArgs

def config():
	args = getProgramArgs()
	fp   = file(args.get('-c'))
	logs = yaml.load(fp)
	fp.close
	return { "logs": logs, "args": args }
