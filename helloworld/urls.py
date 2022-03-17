from django.contrib import admin
from django.urls import path
from .views import HomePage
from .views import ResultPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePage),
    path('result page/',ResultPage),
]
