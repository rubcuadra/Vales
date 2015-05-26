from django import forms
from .models import Person ,Group

class PersonForm(forms.ModelForm):
	def save(self, user, *args, **kwargs):
		self.instance.user = user
		super(PersonForm, self).save(*args, **kwargs)

	class Meta:
		model = Person
		exclude = ('user', )
		# fields
class GroupForm(forms.ModelForm):
	def save(self,user,*args,**kwargs):
		self.instance.user = user
		super(GroupForm, self).save(*args, **kwargs)
	
	def __init__(self, *args, **kwargs):
		user = kwargs.pop('usuario')
		super(GroupForm, self).__init__(*args, **kwargs)
		self.fields['person'].queryset = Person.objects.filter(user = user)

	class Meta:
		model = Group
		exclude = ('user', )
