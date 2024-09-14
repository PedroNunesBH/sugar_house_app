from django.urls import path
from confectionery.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home")
]