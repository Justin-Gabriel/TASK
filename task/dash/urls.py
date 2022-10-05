from django.urls import path
from . import views
from.views import well_data_view

urlpatterns = [
    path('data', views.well_data_view),
]
