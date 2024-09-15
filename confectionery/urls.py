from django.urls import path
from confectionery.views import HomeView, AboutUsView, ContactView, MenuView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("sobre-nos/", AboutUsView.as_view(), name="sobre_nos"),
    path("contato/", ContactView.as_view(), name="contato"),
    path("cardapio/", MenuView.as_view(), name="cardapio")
]