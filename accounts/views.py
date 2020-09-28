from django.contrib.auth import authenticate, login, get_user_model

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.http import is_safe_url

from django.shortcuts import render

from.forms import LoginForm, RegisterForm


def loginPage(request):
	form = LoginForm(request.POST or None)
	context = {
		'form': form,
	}
	#print(request.user.is_authenticated)
	next_ = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_path = next_post or next_ or None
	if form.is_valid():
		print(form.cleaned_data)
		
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(request, username=username, password=password)
		#print(request.user.is_authenticated)
		if user is not None:
			#print(request.user.is_authenticated)
			login(request, user)
			if is_safe_url(redirect_path, request.get_host()):
				return redirect(redirect_path)
			#context['form'] = LoginForm()
			else:
				return redirect('/')
		else:
			# Return an 'invalid login' error message.
			print('error')
	
	return render(request, 'accounts/login.html', context)

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
	return render(request, 'accounts/register.html', context)
