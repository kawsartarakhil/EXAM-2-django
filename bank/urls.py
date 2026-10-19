from django.urls import path
from .views import Home_view,create_income_view,create_expence_view,update_income_view,update_expence_view,delete_income_view,delete_expence_view
urlpatterns = [
    path('home/',Home_view,name='home'),
    path('create/',create_income_view,name='create'),
    path('expence/',create_expence_view,name='expence'),
    path('update_income/<int:pk>/',update_income_view,name='update_income'),
    path('update_expence/<int:pk>/',update_expence_view,name='update_expence'),
    path('delete_income/<int:pk>/',delete_income_view,name='delete_income'),
    path('delete_expence/<int:pk>/',delete_expence_view,name='delete_expence'),
]