from django.urls import path
from apps.users.views import Saludo

urlpatterns = [
    path('saludo/', Saludo.as_view(), name="saludo"),
]
