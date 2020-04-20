from django.test import TestCase
from .views import about_page


class AboutTest(TestCase):
    """
    Here we'll define the tests that we'll run against our Website models
    """
    def test_str(self):
        test_name = about_page(name='about')
        self. assertEqual(str(test_name), 'about')
