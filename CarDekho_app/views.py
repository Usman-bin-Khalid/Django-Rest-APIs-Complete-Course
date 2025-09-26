from django.shortcuts import render
from .models import CarList, ShowRoomList
from django.http import JsonResponse
from .api_file.serializers import CarSerializer, ShowRoomSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

class Showroom_view(APIView):
     def get(self, request):
         showroom = ShowRoomList.objects.all()
         serializer = ShowRoomSerializer(showroom, many=True) 
         return Response(serializer.data)
     def post(self, request):
         serializer = ShowRoomSerializer(data = request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
         else:
             return Response(serializer.errors)

class Showroom_Details(APIView):
    def get(self, request, pk):
        try:
            showroom = ShowRoomList.objects.get(pk = pk)
        except ShowRoomList.DoesNotExist:
            return Response({'Error' , 'Showroom not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ShowRoomSerializer(showroom)
        return Response(serializer.data)
    def put(self, request, pk):
        showroom = ShowRoomList.objects.get(pk = pk)
        serializer = ShowRoomSerializer(showroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        showroom = ShowRoomList.objects.get(pk = pk)
        showroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        

         
         
         
# from django.http import HttpResponse
# import json
# Create your views here.
# def car_list_view(request):
#   cars = CarList.objects.all()
#   data = {
#     'cars' : list(cars.values()),
#   }
#   data_json = json.dumps(data)
#   return HttpResponse(data_json, content_type = 'application/json')
#   # return JsonResponse(data)
# def car_detail_view(request , pk):
#   car = CarList.objects.get(pk=pk)
#   data = {
#     'name' : car.name,
#     'description' : car.description,
#     'active' : car.active
#   }
#   return JsonResponse(data)

@api_view(['GET', 'POST'])
def car_list_view(request):
  if request.method == 'GET':
      car = CarList.objects.all()
      serializer = CarSerializer(car, many = True)
      return Response(serializer.data)
  
  if request.method == "POST":
      serializer = CarSerializer(data = request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      else:
         return Response(serializer.errors)




    
            
   
       

@api_view(['GET' , 'PUT' , 'DELETE'])

def car_detail_view(request, pk):
  if request.method == "GET":
      try:
         
          car = CarList.objects.get(pk = pk)
      except:
          return Response({'Error' : 'car not found'}, status=status.HTTP_404_NOT_FOUND)    
      serializer = CarSerializer(car)
      return Response(serializer.data)
  if request.method == "PUT":
      car = CarList.objects.get(pk = pk)
      serializer = CarSerializer(car , data = request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      else:
         return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
  if request.method == 'DELETE':
      car = CarList.objects.get(pk = pk)   
      car.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    
  

        
