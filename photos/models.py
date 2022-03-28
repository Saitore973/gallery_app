from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)
    location_country = models.CharField(max_length=30)
    location_contact = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def save_location(self):
            self.save()

    def delete_location(self):
        self.delete()


    class Meta:
            ordering = ['name']

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()    

    @classmethod
    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

class Image(models.Model):
    image_name = models.CharField(max_length =30)
    Details = models.TextField()
    photo_credits = models.CharField(max_length =30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category=models.ManyToManyField(Category)
    upload_date = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to = 'images/', null=True)

    # @classmethod
    # def todays_photos(cls):
    #     today = dt.date.today()
    #     photos = cls.objects.filter(upload_date__date = today)
    #     return photos

    # @classmethod
    # def days_photos(cls,date):
    #     photos = cls.objects.filter(upload_date__date = date)
    #     return photos

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location__name__icontains=location)
        return images

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    