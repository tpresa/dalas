import sys
from django.core.management import setup_environ
sys.path.append('/usr/local/dalas/')
import settings
setup_environ(settings)
from dalas.maillog.models import Idlist
from dalas.maillog.models import Msg




#import models from main project...






#list all Msg

m = Msg.objects.all()

for r in m:
	print r
    

