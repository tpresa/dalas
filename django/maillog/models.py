from django.db import models



class Msg(models.Model):
	HostName = models.CharField(max_length=250,blank=True)
	From = models.CharField(max_length=250,blank=True)
	subject = models.CharField(max_length=250,blank=True)
	msgStart = models.DateTimeField(auto_now=True)
	msgEnd = models.DateTimeField(null=True,blank=True)
	size= models.IntegerField(null=True,blank=True)
	checkin = models.DateTimeField(auto_now_add=True,editable=False)
	
	
	def __unicode__(self):
		return self.From


class MsgId(models.Model):
	label = models.CharField(max_length=250,default=u'',blank=True)
	msgid = models.CharField(max_length=250)
	ident = models.ForeignKey(Msg)
	checkin = models.DateTimeField(auto_now_add=True,editable=False)	
	
	def __unicode__(self):
		return "%s [ %s ]" % (self.ident,self.label)



class TypeOfState(models.Model):
	label = models.CharField(max_length=250)
	checkin = models.DateTimeField(auto_now_add=True,editable=False)

	def __unicode__(self):
		return self.label


class TypeOfEvent(models.Model):
	label = models.CharField(max_length=250,default=u'',blank=True)
	checkin = models.DateTimeField(auto_now_add=True,editable=False)

	def __unicode__(self):
		return self.label







class Recipient(models.Model):
	label = models.CharField(max_length=250,default=u'',blank=True)
	emailTo =models.CharField(max_length=250,default=u'',blank=True)
	status = models.ForeignKey(TypeOfState)
	ident = models.ForeignKey(Msg)
	checkin = models.DateTimeField(auto_now_add=True,editable=False)

	def __unicode__(self):
		return "%s [ %s ]" % (self.ident,self.label)
	
	
	
			


	
 
 
class Reject(models.Model):
	label = models.CharField(max_length=250,default=u'',blank=True)
	ident = models.ManyToManyField(MsgId,blank=True)
	checkin = models.DateTimeField(auto_now_add=True,editable=False)
	
	
	
	
	
	

class Event(models.Model):
	label = models.CharField(max_length=250,default=u'',blank=True)
	ident = models.ManyToManyField(MsgId,blank=True)
	type = models.ForeignKey(TypeOfEvent)
	checkin = models.DateTimeField(auto_now_add=True,editable=False)
	
	
	
	
	
	
