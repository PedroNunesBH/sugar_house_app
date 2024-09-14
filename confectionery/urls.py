from django.urls import path
from confectionery.views import HomeView, AboutUsView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("sobre-nos/", AboutUsView.as_view(), name="sobre_nos")
]