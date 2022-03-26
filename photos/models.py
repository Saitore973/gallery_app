from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=30)
    location_country = models.CharField(max_length=30)
    location_contact = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        

            return self.location_name

    class Meta:
            ordering = ['location_name']

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Image(models.Model):
    image_name = models.CharField(max_length =30)
    Details = models.TextField()
    photo_credits = models.CharField(max_length =30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category=models.ManyToManyField(Category)
    upload_date = models.DateTimeField(auto_now_add=True, null=True)

    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        photos = cls.objects.filter(upload_date__date = today)
        return photos

    @classmethod
    def days_photos(cls,date):
        photos = cls.objects.filter(upload_date__date = date)
        return photos