from django.conf.urls import url, include
from .views import all_websites


urlpatterns = [
    url(r'^$', all_websites, name='websites'),
]