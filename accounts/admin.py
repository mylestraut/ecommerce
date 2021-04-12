from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import GuestEmail
from .forms import UserAdminCreationForm #UserAdminChangeForm

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
	search_fields = ['email']
	#form = UserAdminChangeForm
	add_form = UserAdminCreationForm

	# class Meta:
	# 	model = User

admin.site.register(User, UserAdmin)

class GuestEmailAdmin(admin.ModelAdmin):
	search_fields = ['email']
	class Meta:
		model = GuestEmail

admin.site.register(GuestEmail, GuestEmailAdmin)