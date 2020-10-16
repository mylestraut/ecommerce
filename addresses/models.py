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

	def get_address(self):
		return "{line1}\n{line2}\n{city}\n{province}\n{country}\n{postal}".format(
				line1=self.address_line_1,
				line2=self.address_line_2 or "",
				city=self.city,
				province=self.province,
				country=self.country,
				postal=self.postal_code
			)