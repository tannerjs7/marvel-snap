from django.urls import path
from . import views


app_name = 'snap'
urlpatterns = [
    path('', views.index, name='index'),
    path('stats/', views.stats, name='stats'),
    path('<str:card_name>/toggle_owned/', views.toggle_owned, name='toggle_owned'),
    path('add_card/', views.add_card, name='add_card'),
]