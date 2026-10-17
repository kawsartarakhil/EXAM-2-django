from django.urls import path
from .views import Home_view,create_income_view
urlpatterns = [
    path('home/',Home_view,name='home'),
    path('create/',create_income_view,name='create')
]