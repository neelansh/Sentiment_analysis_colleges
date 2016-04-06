from django.db import models

# Create your models here.
class pages(models.Model):
	page_id = models.BigIntegerField()
	page_name = models.CharField(max_length = 100 , default='')
	page_category = models.CharField(max_length = 100 , default='')
	page_posts_json = models.TextField(max_length=2048 , default='')
	page_likes = models.IntegerField()
	def __str__(self):
		return self.page_name
