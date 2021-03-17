from django.contrib.auth import authenticate, login, get_user_model

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from.forms import ContactForm

def homePageView(request):

	print(request.session.get('first_name', 'unknown'))
	context = {
		'title':'Home Page',
		'content': 'This is the home page.',
	}
	if request.user.is_authenticated:
		context['premium_content'] = 'YEEEAAHHHH'
	return render(request, 'homePage.html', context)

def aboutPageView(request):
	context = {
		'title':'About Page',
		'content': 'This is the about page.'
	}
	return render(request, 'homePage.html', context)

def contactPageView(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		'title':'Conatct Page',
		'content': 'This is the conatct page.',
		'form': contact_form,
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
		if request.is_ajax():
			return JsonResponse({"message" : "Thank you for your submission."})

	if contact_form.errors:
		errors = contact_form.errors.as_json()
		if request.is_ajax():
			return HttpResponse(errors, status=400, content_type='application/json')
	# if request.method == 'POST':
	# 	#print(request.POST)
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))
	return render(request, 'contact/view.html', context)























