from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
	"""A book the user is interested in"""
	name = models.CharField(max_length=80) 
	authors = models.JSONField
	year_published = models.IntegerField()
	date_added = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		"""return string representation of the book model"""
		return self.name
		
class Review(models.Model):
	"""Here we enter the review of the book the user entered previously"""
	my_review = models.TextField()
	unfinished = models.BooleanField()
	date_added = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now_add=True)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	
	class Meta:
		""" meta class is added within the class Review, it holds extra information for managing a model."""
		""" Meta class allows us to set a special attribute reviews when we need to enter more than one review"""
		verbose_name_plural = 'reviews'
		
	def __str__(self):
		""" returning a string that represents a model, here - Review"""
		return f"{self.my_review[:50]}..."
		
