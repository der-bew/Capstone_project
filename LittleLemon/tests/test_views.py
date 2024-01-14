from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from Restaurant.models import Menu
from Restaurant.serializers import MenuItemSerializer

class MenuItemsViewTest(TestCase):
    def setUp(self):
       self.menu1 = Menu.objects.create(name='Test Menu 1')
       self.menu2 = Menu.objects.create(name='Test Menu 2')
       self.menu3 = Menu.objects.create(name='Test Menu 3')
       self.list_url = reverse('restaurant/menu')
    def test_getall(self):
       response = self.client.get(self.list_url)
       menus = Menu.objects.all()
       serializer = MenuItemSerializer(menus, many=True)
       self.assertEqual(response.data, serializer.data)
       self.assertEqual(response.status_code, status.HTTP_200_OK)