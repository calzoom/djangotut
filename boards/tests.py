from django.test import TestCase
from django.urls import resolve
from django.core.urlresolvers import reverse

from .views import home

# Create your tests here.


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        # Root URL / should return the home view function
        view = resolve("/")
        self.assertEquals(view.func, home)