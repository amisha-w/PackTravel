from django.test import SimpleTestCase
from django.urls import reverse, resolve
from publish.views import publish_index, display_ride,create_route,select_route


class TestUrl(SimpleTestCase):

    def test_publish_index_resolved(self):
        url = reverse('publish')
        self.assertEquals(resolve(url).func, publish_index)

    def test_create_ride_resolved(self):
        url = reverse('create_route')
        self.assertEquals(resolve(url).func, create_route)

    def test_login_resolved(self):
        url = reverse('select_route')
        self.assertEquals(resolve(url).func, select_route)

    # def test_add_route_resolved(self):
    #     url = reverse('add_route')
    #     self.assertEquals(resolve(url).func, add_)

