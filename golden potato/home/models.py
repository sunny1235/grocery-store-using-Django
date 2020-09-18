from django.db import models

class product(models.Model):
	prId = models.AutoField(primary_key = True)
	prName = models.CharField(max_length=30, default="")
	prDesc = models.CharField(max_length = 300, default = "")
	prImg  = models.ImageField(upload_to = 'home/img', default = "")
	prPrice = models.IntegerField(default=0)
	prDate = models.DateField()
	mainCat = models.CharField(max_length = 20, default="")
	featuredCat = models.CharField(max_length=20, default="")
	onOfferCat = models.CharField(max_length=20, default="")
	latestPrCat = models.CharField(max_length=20, default="")
	topRatedPrCat = models.CharField(max_length=20, default="")
	
	def __str__(self):
		return self.prName
