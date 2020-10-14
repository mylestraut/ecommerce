from django import forms

from .models import Address

class AddressForm(forms.ModelForm):

	#address_type = forms.CharField(widget=forms.HiddenInput())


	class Meta:
		model = Address
		fields = [
			#'billing_profile',
			#'address_type',
			'address_line_1',
			'address_line_2',
			'city',
			'province',
			'country',
			'postal_code',
		]
