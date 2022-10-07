from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('data', views.well_data_view),
]
