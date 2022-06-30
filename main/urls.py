from django.urls import path
from main.views import project_info

urlpatterns = [
    path('', project_info),
]