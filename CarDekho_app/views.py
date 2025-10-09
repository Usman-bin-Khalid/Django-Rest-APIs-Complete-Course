from django.shortcuts import render
from .models import CarList, ShowRoomList, Review
from django.http import JsonResponse
from .api_file.serializers import CarSerializer, ShowRoomSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissions
from django.shortcuts import get_object_or_404
from rest_framework import mixins

from rest_framework import viewsets
from rest_framework import generics


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer    


# class ReviewDetails(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     # Only saw information but you can not update or delete information
#     # Using DjangoModelPermissions
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [DjangoModelPermissions]
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

class Showroom_Viewset(viewsets.ModelViewSet):
     queryset = ShowRoomList.objects.all()
     serializer_class = ShowRoomSerializer
     
# class Showroom_Viewset(viewsets.ViewSet):
#      def list(self, request):
#          queryset = ShowRoomList.objects.all()
#          serializer = ShowRoomSerializer(queryset, many=True,
#          context={'request': request} )
#          return Response(serializer.data)

#      def retrieve(self, request, pk=None):
#          queryset = ShowRoomList.objects.all()
#          user = get_object_or_404(queryset, pk=pk)
#          serializer = ShowRoomSerializer(user,
#                                          context={'request': request})
#          return Response(serializer.data)
     
#      def create(self, request):
#          serializer = ShowRoomSerializer(data = request.data)
#          if serializer.is_valid():
#             serializer.save()
            
#             return Response(serializer.data)
#          else:
#             return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class Showroom_view(APIView):
    #  authentication_classes = [BasicAuthentication]
    #  permission_classes = [IsAuthenticated] # Only Authenticated User can access data
    #  permission_classes = [AllowAny] # Any user without authentication can access data
    #  permission_classes = [IsAdminUser] # Only Admin can access data
    # Session Authentication ko apply krny ky liy phly admin to logout krna pry ga
     authentication_classes = [SessionAuthentication]
     permission_classes = [IsAuthenticated]

     def get(self, request):
         showroom = ShowRoomList.objects.all()
         serializer = ShowRoomSerializer(showroom, many=True, context={'request': request}) 
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
    
  

        
class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ReviewList(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)    
