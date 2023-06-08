from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("convert_pdf/", views.convert_pdf, name="convert_pdf"),
]