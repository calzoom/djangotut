from django.test import TestCase
from django.urls import resolve
from django.core.urlresolvers import reverse

from .views import home, board_topics
from .models import Board

# Create your tests here.


class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name="Django", description="Django board.")
        url = reverse("home")
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        # Root URL / should return the home view function
        view = resolve("/")
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        # testing if response body has "href=/boards/1/"
        board_topics_url = reverse("board_topics", kwargs={"pk": self.board.pk})
        self.assertContains(self.response, f'href="{board_topics_url}"')


class BoardTopicsTests(TestCase):
    # Django testing suite doesn't run tests against current database
    def setUp(self):
        Board.objects.create(name="Django", description="Django board.")

    # status code tests
    def test_board_topics_view_success_status_code(self):
        url = reverse("board_topics", kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse("board_topics", kwargs={"pk": 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    # test the view function
    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve("/boards/1/")
        self.assertEquals(view.func, board_topics)

    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url = reverse("board_topics", kwargs={"pk": 1})
        response = self.client.get(board_topics_url)
        homepage_url = reverse("home")
        self.assertContains(response, f'href="{homepage_url}"')