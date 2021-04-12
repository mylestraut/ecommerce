from django import forms

from .models import User

from django.contrib.auth import get_user_model

from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


# class UserAdminChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = User
#         fields = ['email', 'password', 'is_active', 'admin']

#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]



class GuestForm(forms.Form):
	email = forms.EmailField()

class LoginForm(forms.Form):
	email 		= forms.EmailField(label='Email')
	password	= forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        #user.active = False # Send confirmation email
        if commit:
            user.save()
        return user

# class RegisterForm(forms.Form):
# 	#username 	= forms.CharField()
# 	email		= forms.EmailField()
# 	password	= forms.CharField(widget=forms.PasswordInput)
# 	password2	= forms.CharField(label = 'Conform Password', widget=forms.PasswordInput)

# 	def clean_username(self):
# 		username = self.cleaned_data.get('username')
# 		qs = User.objects.filter(username=username)
# 		if qs.exists():
# 			raise forms.ValidationError('Username taken')
# 		return username

# 	def clean_email(self):
# 		email = self.cleaned_data.get('email')
# 		qs = User.objects.filter(email=email)
# 		if qs.exists():
# 			raise forms.ValidationError('email is taken')
# 		return email

# 	def clean(self):
# 		data = self.cleaned_data
# 		password = self.cleaned_data.get('password')
# 		password2 = self.cleaned_data.get('password2')
# 		if password2 != password:
# 			raise forms.ValidationError("Passwords don't match")
# 		return data