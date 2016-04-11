from django.db import models

# Create your models here.
class pages(models.Model):
	institute_name = models.CharField(max_length = 100 , default = '')
	page_id = models.BigIntegerField()
	page_name = models.CharField(max_length = 100 , default='' , null = True)
	page_category = models.CharField(max_length = 100 , default='', null = True)
	page_posts_json = models.TextField(max_length=8000 , default='', null = True)
	page_likes = models.IntegerField()
	page_json = models.TextField(max_length = 8000 , default = "")
	class Meta:
		unique_together = ["institute_name" , "page_id"]
	def __str__(self):
		return self.page_name


class twitter(models.Model):
	institute_name = models.CharField(max_length = 100 , default = '' , unique = True)
	twitter_json = models.TextField(max_length = 8000 , default = "")
	def __str__(self):
		return self.institute_name

class tweets(models.Model):
	tweet_id = models.BigIntegerField()
	favorited = models.BooleanField()
	favorite_count = models.IntegerField()
	retweeted = models.BooleanField()
	retweet_count = models.IntegerField()
	source = models.CharField(max_length = 200)
	text = models.CharField(max_length = 200)
	user_name = models.CharField(max_length = 100)
	user_id = models.BigIntegerField()
	institute = models.ForeignKey('twitter')
	def __str__(self):
		return self.user_name


class fullform(models.Model):
	short_form = models.CharField(max_length = 50 , default = "" , unique = True)
	full_form = models.CharField(max_length = 100 , default = "")
	def __str__(self):
		return self.short_form