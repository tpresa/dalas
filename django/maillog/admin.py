
from django.contrib import admin


from dalas.maillog.models import *





admin.site.register(TypeOfEvent)
admin.site.register(TypeOfState)

admin.site.register(Reject)

admin.site.register(Recipient)

admin.site.register(Event)    
    
admin.site.register(MsgId)
admin.site.register(Msg)
