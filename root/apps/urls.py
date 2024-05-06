from django.urls import path
from apps.views import news, contact, home

urlpatterns = [
    path('news', news, name='news'),
    path('contact', contact, name='contact'),
    path('', home, name='home')

]
