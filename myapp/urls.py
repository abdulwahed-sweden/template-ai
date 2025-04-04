# myapp/urls.py

from django.urls import path
from .views import home, immigration_advisor

urlpatterns = [
    path('', home, name='home'),
    path('immigration/', immigration_advisor, name='immigration_advisor'),
]
