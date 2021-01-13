from .views import UserCreateView
from django.urls import path


urlpatterns = [
    path('create', UserCreateView.as_view(), name='create_user')
]
