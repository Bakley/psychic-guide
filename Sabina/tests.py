from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase

from .views import home
# Create your tests here.


class HomeTests(TestCase):
    """Home Views test"""

    def test_home_view_status(self):
        """Testing the home page view url"""
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_reolves_home_view(self):
        """Test whether the home url / resolvers to the home view"""
        view = resolve('/')
        self.assertEquals(view.func, home)
