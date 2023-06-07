from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("image/", views.image, name="image"),
    path("convert_pdf/", views.convert_pdf, name="convert_pdf"),
]