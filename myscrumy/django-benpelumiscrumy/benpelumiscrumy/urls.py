# from django.urls import path
# from benpelumiscrumy import views


# urlpatterns = [
#     path('', views.homePage, name='home'),
# ]

from django.urls import path
from .views import homePage


urlpatterns = [
    path('', homePage, name='home'),
]