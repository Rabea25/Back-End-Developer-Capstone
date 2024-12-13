from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_create_item(self):
        item = Menu.objects.create(title='Pizza', price=10.00, inventory=10)
        self.assertEqual(item.title, 'Pizza')
        self.assertEqual(item.price, 10.00)

    def test_get_item(self):
        item = Menu.objects.create(title='Pizza', price=10.00, inventory=10)
        self.assertEqual(item, Menu.objects.get(title='Pizza'))