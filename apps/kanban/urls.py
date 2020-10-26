from django.urls import path
from .views import KanbanHomePage


urlpatterns = [
    path('', KanbanHomePage.as_view(), name='home')
]
