from django.db import models

from billing.models import BillingProfile

ADDRESS_TYPES = (
	('shipping','Shipping'),
	('billing','Billing'),
)
class Address(models.Model):
	billing_profile = models.ForeignKey(BillingProfile, on_delete=models.DO_NOTHING)
	address_type 	= models.CharField(max_length=120, choices=ADDRESS_TYPES)
	address_line_1	= models.CharField(max_length=120)
	address_line_2	= models.CharField(max_length=120, blank=True, null=True)
	city			= models.CharField(max_length=120)
	province		= models.CharField(max_length=120)
	country			= models.CharField(max_length=120, default='South Africa')
	postal_code		= models.CharField(max_length=120)

	def __str__(self):
		return str(self.billing_profile)