from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls, name = 'admin'),
    path("", include("reserv_app.urls")),
    path("", include("auth_app.urls")),

]