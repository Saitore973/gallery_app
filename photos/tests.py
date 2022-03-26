from django.test import TestCase
from .models import Location,Image,Category
import datetime as dt
# Create your tests here.




class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.nairobi= Location(location_name = 'Nairobi', location_country ='Kenya')
        self.nairobi.save_location()

        # Creating a new tag and saving it
        self.new_category = Category(name = 'testing')
        self.new_category.save()

        self.new_image= Image(image_name = 'Test Image',details = 'This is a random test ', photo_credits='test', Location = self.nairobi)
        self.new_image.save()

        self.new_image.category.add(self.new_category)

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

def test_get_photos_today(self):
        today_photos = Image.todays_photos()
        self.assertTrue(len(today_photos)>0)

def test_get_photos_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        photos_by_date = Image.days_photos(date)
        self.assertTrue(len(photos_by_date) == 0)