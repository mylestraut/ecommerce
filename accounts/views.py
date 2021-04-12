from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import CreateView, FormView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.http import is_safe_url

from django.shortcuts import render

from.forms import LoginForm, RegisterForm, GuestForm

from .models import GuestEmail

def guest_register_view(request):
	form = GuestForm(request.POST or None)
	context = {
		'form': form,
	}
	
	next_ = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_path = next_post or next_ or None
	if form.is_valid():
		
		email = form.cleaned_data.get('email')
		new_guest_email = GuestEmail.objects.create(email=email)
		request.session['guest_email_id'] = new_guest_email.id

		if is_safe_url(redirect_path, request.get_host()):
			return redirect(redirect_path)		
		else:
			return redirect('/register/')
	
	return redirect('/register/')

class LoginView(FormView):
	form_class = LoginForm
	success_url = "/"
	template_name = 'accounts/login.html'

	def form_valid(self, form):
		request = self.request
		next_ = request.GET.get('next')
		next_post = request.POST.get('next')
		redirect_path = next_post or next_ or None

		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		user = authenticate(request, username=email, password=password)
		#print(request.user.is_authenticated)
		if user is not None:
			#print(request.user.is_authenticated)
			login(request, user)
			try:
				del request.session['guest_email_id']
			except:
				pass
			if is_safe_url(redirect_path, request.get_host()):
				return redirect(redirect_path)
			#context['form'] = LoginForm()
			else:
				return redirect('/')
		return super(LoginView, self).form_invalid(form)

# def loginPage(request):
# 	form = LoginForm(request.POST or None)
# 	context = {
# 		'form': form,
# 	}
# 	#print(request.user.is_authenticated)
# 	next_ = request.GET.get('next')
# 	next_post = request.POST.get('next')
# 	redirect_path = next_post or next_ or None
# 	if form.is_valid():
# 		print(form.cleaned_data)
		
# 		username = form.cleaned_data.get('username')
# 		password = form.cleaned_data.get('password')
# 		user = authenticate(request, username=username, password=password)
# 		#print(request.user.is_authenticated)
# 		if user is not None:
# 			#print(request.user.is_authenticated)
# 			login(request, user)
# 			try:
# 				del request.session['guest_email_id']
# 			except:
# 				pass
# 			if is_safe_url(redirect_path, request.get_host()):
# 				return redirect(redirect_path)
# 			#context['form'] = LoginForm()
# 			else:
# 				return redirect('/')
# 		else:
# 			# Return an 'invalid login' error message.
# 			print('error')
	
# 	return render(request, 'accounts/login.html', context)

class RegisterView(CreateView):
	form_class = RegisterForm
	template_name = 'accounts/register.html'
	success_url = "/login/"

# User = get_user_model()

# def registerPage(request):
# 	form = RegisterForm(request.POST or None)
# 	context = {
# 		'form': form,
# 	}
	
# 	if form.is_valid():
# 		form.save()

# 	return render(request, 'accounts/register.html', context)
