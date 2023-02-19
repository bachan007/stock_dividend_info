from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('search_result',views.search_result, name='search_result')
]