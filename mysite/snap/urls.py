from django.urls import path
from . import views


app_name = 'snap'
urlpatterns = [
    path('cards/', views.index, name='index'),
    path('cards/<str:filter>/', views.index, name='filter'),
    path('stats/', views.stats, name='stats'),
    path('spotlights/', views.spotlights, name='spotlights'),
    path('<str:card_name>/toggle_owned/', views.toggle_owned, name='toggle_owned'),
    path('add_card/', views.add_card, name='add_card'),
]