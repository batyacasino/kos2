from random import randint
from transliterate import translit
from re import findall
from datetime import date, timedelta

from .models import *
from .yandex_pdd import app

def clients_list_email(clients):
	clients_list_email = []
	for client in clients:
		reminder = Reminder.objects.filter(client_id=client.id)
		if reminder:
			for rem in reminder:	
				days_to_reminder = str(rem.date_completion - date.today())[0]
				if int(days_to_reminder) <= 0:		
					remind = {
						'id': client.id,
						'description': rem.description,
						'days_to_reminder': days_to_reminder,
					}
					clients_list_email.append(remind)
		email_count = app.email_counters(client.email[:-15])
		if email_count['unread'] != 0:
			client_dict = {
				'id': client.id,
				'claimant': client.claimant,
				'defendant': client.defendant,
				'email_count': email_count['unread']
			}
			clients_list_email.append(client_dict)
	return clients_list_email


def email_login(claimant):
	find_name = findall(r'[\w]+', claimant)
	unique_login = randint(1, 1000000)
	try:
		last_name = translit(find_name[0], reversed=True)
	except:
		last_name = find_name[0]
	return f'{last_name}{unique_login}'


def email_password():
	password = ''
	for n in range(randint(10, 16)):
		printable = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*'
		x = randint(0, len(printable) - 1)
		password += printable[x]
	return password