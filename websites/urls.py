from django.conf.urls import url
from .views import all_websites


urlpatterns = [
    url(r'^$', all_websites, name='websites'),
]
