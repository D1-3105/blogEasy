from django.urls import path, include
from .views import PostView
urlpatterns = [
    path('', PostView.as_view(), name="home"),
]