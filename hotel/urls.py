from django.contrib import admin
from django.urls import path
from reservas.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]