from django.contrib.auth.models import User
from rest_framework import serializers
class RegisterSerializer(serializers.ModelSerializer):
  password_confirmation = serializers.CharField(style={'input_type' : 'password'}, write_only = True)
  class Meta:
    model = User
    fields = ['username' , 'email' , 'password' , 'password_confirmation']
    extra_kwargs = {
      'password' : {'write_only' : True}
    }

  def save(self):
    password = self.validated_data['password']
    password2 = self.validated_data['password_confirmation'] 
    if password != password2:
      raise serializers.ValidationError({'error' : 'Password and Confirm Password Must be Same'})
    if User.objects.filter(email = self.validated_data['email']).exists():
      raise serializers.ValidationError({'error' : 'Email Already Exists'})

    account = User(email = self.validated_data['email'] , username = self.validated_data['username'])
    account.set_password(password)
    account.save()
    return account 
  

