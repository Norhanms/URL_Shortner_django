from django.urls import path
from .views import dashboard, stats
urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('<str:alias>/stats', stats, name="stats")

]
