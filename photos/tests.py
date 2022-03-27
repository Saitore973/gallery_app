from django.test import TestCase
from .models import Location,Image,Category
import datetime as dt
# Create your tests here.




class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.nairobi= Location(name = 'Nairobi', location_country ='Kenya')
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

    # def test_get_photos_today(self):
    #         today_photos = Image.todays_photos()
    #         self.assertTrue(len(today_photos)>0)

    # def test_get_photos_by_date(self):
    #         test_date = '2017-03-17'
    #         date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
    #         photos_by_date = Image.days_photos(date)
    #         self.assertTrue(len(photos_by_date) == 0)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'photos/test.jpg')
        changed_img = Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)

    def test_get_image_by_id(self):
        found_image = self.image_test.get_image_by_id(self.image_test.id)
        image = Image.objects.filter(id=self.image_test.id)
        self.assertTrue(found_image, image)

    def test_filter_by_location(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_location(location='moringa')
        self.assertTrue(len(found_images) == 1)

    def test_search_by_category(self):
        category = 'home'
        found_img = self.image_test.search_by_category(category)
        self.assertTrue(len(found_img) > 1)



class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(name='Moringa')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.locations()
        self.assertTrue(len(locations) > 0)

   
    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='home')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)