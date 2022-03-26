from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=30)
    location_country = models.CharField(max_length=30)

    def __str__(self):
        try:
            location = Location.objects.get(email = 'example@gmail.com')
            print('Editor found')
        except DoesNotExist:
            print('Editor was not found')

            return self.location_name

    class Meta:
            ordering = ['location_name']

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Image(models.Model):
    image_name = models.CharField(max_length =30)
    post = models.TextField()
    photo_credits = models.CharField(max_length =30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)