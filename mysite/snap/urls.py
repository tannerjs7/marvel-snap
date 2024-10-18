from django.urls import path
from . import views


app_name = 'snap'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:sort_column>/<str:sort_type>/sort', views.index, name='sort'),
    path('<str:card_name>/toggle_owned/', views.toggle_owned, name='toggle_owned'),
    path('add_card/', views.add_card, name='add_card'),
    # path('<str:sort_column>/<str:sort_type>', views.sort_cards, name='sort_cards'),
]