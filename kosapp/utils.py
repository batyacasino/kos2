from django.shortcuts import render, get_object_or_404
from datetime import date, timedelta

from .models import *
from .forms import *

class ObjectDetailMixin:
	model = None
	template = None

	def get(self, request, pk):
		obj = get_object_or_404(self.model, pk=pk)
		email_count = app.email_counters(obj.email[:-15])
		files = ClientDocs.objects.filter(client_id=pk)
		reminder = Reminder.objects.filter(client_id=pk)
		if reminder:
			for rem in reminder:	
				days_to_reminder = str(rem.date_completion - date.today())[0]				
				remind = {
					'id': rem.id,
					'description': rem.description,
					'days_to_reminder': days_to_reminder,
				}
		else:
			remind = reminder
				
		


		return render(request, 'kosapp/detail_client.html', {
																"client": obj, 
																"files": files,
																'email_count':email_count,
																'remind': remind
												})


'''	
	for rem in reminder:
			r = 
			print(str(r))
'''
#today = date.today()
#next_month_date = today + timedelta(days=2)
#print(next_month_date)
	
