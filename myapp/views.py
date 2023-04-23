from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import musicDatabased
from .serializer import myData
from django.http import HttpResponse
from .forms import Post

@api_view(["GET"])
def get_request(request):
  data = musicDatabased.objects.all()
  x = myData(data, many=True)
  return Response(x.data)
  
@api_view(["POST"])
def add_data(request):
  serializer = myData(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)
  