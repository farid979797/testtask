from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('<int:menuitem_id>/', categories, name='menuitem')
]
