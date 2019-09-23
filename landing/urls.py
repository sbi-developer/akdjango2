from django.conf.urls import url, include
from django.contrib import admin
from .views import home, business

app_name = "landing"
urlpatterns = [
    url(r'^', home, name='home'),
    url(r'^for-business', business, name='for-business'),
]