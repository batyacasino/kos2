from django.db import models
from django.shortcuts import reverse

class Client(models.Model):
	date_creat = models.DateField(auto_now_add=True)
	claimant = models.CharField(max_length=200)
	date_of_birth = models.DateField()
	defendant = models.CharField(max_length=200)	
	email = models.EmailField(max_length=200)
	email_password = models.CharField(max_length=200)
	date_of_inspection = models.DateField()

	def __str__(self):
		return self.claimant

	def get_absolut_url(self):
		return reverse('client_list_url', kwargs={'pk':self.id})


class ClientDocs(models.Model):
	client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
	claimant = models.CharField(max_length=200)
	document = models.FileField(upload_to='docs/pdfs/')

	def __str__(self):
		return self.claimant


class Reminder(models.Model):
	client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
	date_creat = models.DateField(auto_now_add=True)
	days_to_completion =  models.IntegerField()
	date_completion =   models.DateField()
	description = models.CharField(max_length=200)




