from django import forms
from django.forms import ModelForm
from datetime import date, timedelta

from .models import *
from .yandex_pdd import app
from .services import *






class ClientForm(forms.Form):
	claimant = forms.CharField(max_length=200)
	date_of_birth = forms.DateField()
	defendant = forms.CharField(max_length=200)
	date_of_inspection = forms.DateField()

	claimant.widget.attrs.update({'class':'form-control', 'placeholder':'Истец'})
	date_of_birth.widget.attrs.update({'type':'date', 'class':'form-control', 'placeholder':'дата рождения: 2000-21-12'})
	defendant.widget.attrs.update({'class':'form-control', 'placeholder':'Ответчик'})
	date_of_inspection.widget.attrs.update({'type':'date', 'class':'form-control', 'placeholder':'дата осмотра: 2000-21-12'})

	def save(self):
		login = email_login(self.cleaned_data['claimant'])
		password = email_password()
		app.email_add(login, password)
		app.email_edit(login=login, fname=login, hintq=login, hinta=password)
		new_client = Client.objects.create(
			claimant = self.cleaned_data['claimant'],
			defendant = self.cleaned_data['defendant'],
			date_of_birth = self.cleaned_data['date_of_birth'],
			email = f'{login}@botpromokot.ru',
			email_password = password,
			date_of_inspection = self.cleaned_data['date_of_inspection'],
		)
		return new_client

class UploadDocsForm(ModelForm):
	class Meta:
		model = ClientDocs
		fields = ('claimant', 'document')
		widgets = {
			"claimant": forms.TextInput(attrs={'class':'form-control text-center', 'placeholder':'Введите название файла'}),
			"document": forms.FileInput(attrs={"class": "custom-file-input", 'type':"file", 'id':"customFileLang", 'lang':"ru"})}


class ReminderForm(ModelForm):
	class Meta:
		model = Reminder
		fields = ('days_to_completion', 'description')


