from django.urls import path
from .views import hello_world

urlpatterns = [
    path('app/',hello_world),
    

]
