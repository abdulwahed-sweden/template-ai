# myapp/urls.py

from django.urls import path
from .views import immigration_advisor

urlpatterns = [
    path('immigration/', immigration_advisor, name='immigration_advisor'),
]
