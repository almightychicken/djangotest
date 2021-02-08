from django.test import TestCase, RequestFactory
from . import views
# Create your tests here.

class Tests(TestCase):

	def setUp(self):
		self.factory = RequestFactory()

	def test_redirect_view(self):
		request = self.factory.get('/')
		self.assertEqual(302, views.index(request).status_code)
