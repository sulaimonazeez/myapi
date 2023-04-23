from django.urls import path
from . import views
urlpatterns = [
  path('', views.get_request, name="get_data"),
  path('add/',views.add_data, name="add_data"),
]