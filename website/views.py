from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message_subject = request.POST['message-subject']
		message = request.POST['message']

		# send an email
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from email
			['i.nyamu5@gmail.com'], # to email

			)

		return render(request, 'contact.html', {'message_name': message_name})
	else:	
		return render(request, 'contact.html', {})

def blog(request):
	return render(request, 'blog.html', {})

def about(request):
	return render(request, 'about.html', {})

def service(request):
	return render(request, 'service.html', {})

def portfolio(request):
	return render(request, 'portfolio.html', {})

def single(request):
	return render(request, 'single.html', {})

def team(request):
	return render(request, 'team.html', {})
