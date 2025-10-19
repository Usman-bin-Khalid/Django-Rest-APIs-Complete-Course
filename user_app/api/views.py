from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user_app.api.serializers import RegisterSerializer

@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
          
            user = serializer.save() 
        
            data = {'message': 'Registration successful'} 
            
            return Response(data, status=status.HTTP_201_CREATED)
        
        else:
        
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
