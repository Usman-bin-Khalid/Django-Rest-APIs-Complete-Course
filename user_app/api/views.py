from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from user_app.api.serializers import RegisterSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken



@api_view(['POST'])
def logout_view(request):
    try:
        if request.user.is_authenticated:
            
            if request.auth:
                request.auth.delete() 
            
           
            Token.objects.filter(user=request.user).delete()


            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No user is logged in.'}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
       
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
          
            user = serializer.save() 
        
            data = {'message': 'Registration successful'} 
            refresh = RefreshToken.for_user(user)
            data['token'] = {
                 'refresh': str(refresh),
                 'access': str(refresh.access_token),
            }
            
            return Response(data, status=status.HTTP_201_CREATED)
        
        else:
        
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )

        
