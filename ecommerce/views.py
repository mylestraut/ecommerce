from django.contrib.auth import authenticate, login, get_user_model

from django.shortcuts import render, redirect
from django.http import HttpResponse

from.forms import ContactForm, LoginForm, RegisterForm

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
	# if request.method == 'POST':
	# 	#print(request.POST)
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
	# 	print(request.POST.get('content'))
	return render(request, 'contact/view.html', context)

def loginPage(request):
	form = LoginForm(request.POST or None)
	context = {
		'form': form,
	}
	#print(request.user.is_authenticated)
	if form.is_valid():
		print(form.cleaned_data)
		
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(request, username=username, password=password)
		#print(request.user.is_authenticated)
		if user is not None:
			#print(request.user.is_authenticated)
			login(request, user)
			#context['form'] = LoginForm()
			return redirect('/')
		else:
			# Return an 'invalid login' error message.
			print('error')
	
	return render(request, 'auth/login.html', context)

User = get_user_model()
def registerPage(request):
	form = RegisterForm(request.POST or None)
	context = {
		'form': form,
	}
	
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get('username')
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		new_user = User.objects.create_user(username, email, password)
		print(new_user)
	return render(request, 'auth/register.html', context)





















