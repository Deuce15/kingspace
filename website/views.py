from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})

def contact(request):
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
