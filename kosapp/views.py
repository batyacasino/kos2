from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, ListView
from django.core.files.storage import FileSystemStorage
from random import randint
from datetime import date, timedelta

from .models import *
from .forms import *
from .utils import *
from .services import *

class ClientList(ListView):
	""" Список клиентов """
	model = Client
	queryset = Client.objects.all()

def index(request):
	clients = Client.objects.all()
	clients_list = clients_list_email(clients)
	return render(request, 'kosapp/index.html', {
												"clients_list_email": clients_list,
												'client_count_email': len(clients_list),
												})


def yandex_oauth(request, pk):
	client = Client.objects.get(id=pk)
	link = app.passport_oauth('https://mail.yandex.ru/', email=client.email)
	return render(request, 'kosapp/yandex_oauth.html', {'link':link[1:]})


class ClientDetail(ObjectDetailMixin, View):
	model = Client
	template = 'kosapp/detail_client.html'


class AddClient(View):
	def get(self, request):
		form = ClientForm()
		return render(request, 'kosapp/add_client.html', {"form": form})

	def post(self, request):
		form = ClientForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'kosapp/detail_client.html', {"client": new_client,})			
		return render(request, 'kosapp/add_client.html', {"form": bound_form})


class UploadDocs(View):
	def get(self, request, pk):
		client = Client.objects.get(id=pk)
		form = UploadDocsForm()
		return render(request, 'kosapp/upload_docs.html', {"form": form, "client": client})

	def post(self, request, pk):
		form = UploadDocsForm(request.POST, request.FILES)
		client = Client.objects.get(id=pk)
		if form.is_valid():
			form = form.save(commit=False)
			form.client_id = Client.objects.get(id=pk)
			form.save()
		return redirect(f"/detail_client/{pk}")



class ReminderView(View):
	def get(self, request, pk):
		client = Client.objects.get(id=pk)
		form = ReminderForm()
		return render(request, 'kosapp/reminder.html', {"form": form, "client": client})

	def post(self, request, pk):
		form = ReminderForm(request.POST)
		client = Client.objects.get(id=pk)
		if form.is_valid():
			form = form.save(commit=False)
			form.date_completion =  date.today() + timedelta(days=int(form.days_to_completion))
			form.client_id = Client.objects.get(id=pk)
			form.save()
		return redirect(f"/detail_client/{pk}")

class DeleteReminderView(View):
	def get(self, request, pk):
		reminder = Reminder.objects.get(id=pk)
		print(reminder)
		return render(request, 'kosapp/delete_reminder.html', {"reminder": reminder})
		
	def post(self, request, pk):
		reminder = Reminder.objects.get(id=pk)
		reminder.delete()
		return redirect("/")