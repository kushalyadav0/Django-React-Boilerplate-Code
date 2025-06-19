from django.shortcuts import render
from rest_framework.permissions import AllowAny  
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@AllowAny
@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello from Django!"})
