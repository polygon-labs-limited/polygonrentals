from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200)
    value = models.IntegerField(default=0)
    mortgage = models.IntegerField(default=0)
    current_rent = models.IntegerField(default=0)
    market_rent = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='images/', default='')
    city = models.CharField(max_length=200, default='', choices=[('liverpool', 'Liverpool'), ('manchester', 'Manchester'), ('london', 'London')])
    mortgage_deal_expiry_date = models.DateField(default=date.today)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = "properties"


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='news_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=((0,"Draft"),(1,"Publish")), default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title