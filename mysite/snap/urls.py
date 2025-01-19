from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'snap'
urlpatterns = [
    path('cards/', views.index, name='index'),
    path('cards/<str:filter>/', views.index, name='filter'),
    path('stats/', views.stats, name='stats'),
    path('spotlights/', views.spotlights, name='spotlights'),
    path('decks/', views.decks, name='decks'),
    path('<str:card_name>/toggle_checkboxes/', views.toggle_checkboxes, name='toggle_checkboxes'),
    path('add/', views.add, name='add'),
    path('add_card/', views.add_card, name='add_card'),
    path('add_spotlight/', views.add_spotlight, name='add_spotlight'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]