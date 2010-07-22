#!/usr/bin/python
# -*- coding: utf-8 -*-
# processLog v0.1-20091018
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

from time import sleep
import sys
import traceback
import configPkg
import logPkg

__version__ = "processLog v0.1-20091018"

#
# Exception classes
#

class CANT_OPEN_LOGFILE(Exception):
	pass

class THIS_IS_NOT_A_CLASS(Exception):
	pass

#
# Output exception control
#

ErrorVerbose = False

def TracebackHandle(type, value, tb):
	if ErrorVerbose:
		traceback.print_exception(type, value, tb)
	else:
		print traceback.format_exception_only(type, value)[0].strip()

sys.excepthook = TracebackHandle

#
# process arguments
#

def getProgramArgs():
	def help():
		print """
Usage: %s -c configFile
Options available:
    -c ,    --conf            Path to the configuration file
    -h ,    --help            Show this help
    -v ,    --version         Print program version

Bugs: <reinaldoc@gmail.com>.
		""".strip() % sys.argv[0]
		sys.exit(1)

	def version():
		print __version__
		sys.exit(0)

	readArgs = {"-c": 1}
	lastArg = ""
	for arg in sys.argv[1:]:
		if readArgs.get(lastArg) == 2:
			readArgs[lastArg] = arg
		elif readArgs.get(lastArg) == 1:
			help()
		lastArg = arg

		if arg == '-c' or arg == '--conf':
			readArgs['-c'] = 2
			lastArg = '-c'
		elif arg == '-v' or arg == '--version':
			version()
	
	if type(readArgs.get('-c')) == type(0):
		help()
	return readArgs

# End comment

if __name__ != "__main__":
    raise THIS_IS_NOT_A_CLASS
    sys.exit(1)

programArgs = getProgramArgs()
configObj = configPkg.configInterface(programArgs.get('-c'))
logObj = logPkg.logProcessor()
logObj.setConfig(configObj)
logObj.initialize()

#
#    Create $logfileHandle dictionary with EntryName
# as Key and opened file handle as Value
#

logfileHandle = {}
for logEntryName in configObj.getEntryNamesOfLogfiles():
	try:
		logfileHandle[logEntryName] = open(configObj.getPathByName(logEntryName), "r")
	except:
	    raise CANT_OPEN_LOGFILE(configObj.getPathByName(logEntryName))

#
# Set file handles to end of file
#

for item in logfileHandle.keys():
	logfileHandle[item].seek(0, 2)

# Set up Django's ORM
import sys
from django.core.management import setup_environ
import settings

setup_environ(settings)
from dalas.maillog.models import *


#
# Main code
#

try:
    while True:
		for logfileEntryName in logfileHandle.keys():
			while True:
				line = logfileHandle.get(logfileEntryName).readline()
				if line:
					logObj.insert(logfileEntryName, line.strip())
				else:
					break
		sleep(1)
except KeyboardInterrupt:
    pass

#
# Close file handles
#

for item in logfileHandle.keys():
	logfileHandle[item].close()

#
# End of program
#
