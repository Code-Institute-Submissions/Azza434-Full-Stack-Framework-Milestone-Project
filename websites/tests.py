from django.test import TestCase
from .models import Website


class WebsiteTest(TestCase):
    """
    Here we'll define the tests that we'll run against our Website models
    """

    def test_str(self):
        test_name = Website(name='A website')
        self. assertEqual(str(test_name), 'A website')
