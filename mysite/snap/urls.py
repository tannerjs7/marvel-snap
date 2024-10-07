from django.urls import path
from . import views


app_name = 'snap'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:card_name>/toggle_owned/', views.toggle_owned, name='toggle_owned'),
]