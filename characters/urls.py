from django.urls import path
from characters.views import characters_list

urlpatterns = [
    path('', characters_list),
]