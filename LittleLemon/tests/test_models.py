from django.test import TestCase
from Restaurant.models import Menu

class MenuItemTest(TestCase):
    def get_menu_items(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")    