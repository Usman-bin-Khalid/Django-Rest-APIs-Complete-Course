from rest_framework import serializers
from ..models import CarList, ShowRoomList

def alphanumberic(value):
    if not str(value).isalnum():
       raise serializers.ValidationError("Only alphanumeric characters are allowed")

# class CarSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only = True)
#   name = serializers.CharField()
#   description = serializers.CharField()
#   active = serializers.BooleanField(read_only = True)
#   chassisnumber = serializers.CharField(validators = [alphanumberic])
#   price = serializers.DecimalField(max_digits= 9 , decimal_places= 2)

class ShowRoomSerializer(serializers.ModelSerializer):
  class Meta:
      model = ShowRoomList
      fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
  discounted_price = serializers.SerializerMethodField()

  
  class Meta:
      model = CarList
        #  fields = ['id' , 'name' , 'description'] # for all fields manually
        #  exclude =  ['name'] # Except name all fields
      fields = '__all__' # for All Fields

  def get_discounted_price(self , object):
      discountprice = object.price - 5000
      return discountprice
  

  

#   def create(self, validate_data):
#     return CarList.objects.create(**validate_data)
  

#   def update(self, instance, validated_data):
#       instance.name = validated_data.get('name' , instance.name)
#       instance.description = validated_data.get('description', instance.description)
#       instance.active = validated_data.get('active', instance.active)
#       instance.chassisnumber = validated_data.get('chassisnumber' , instance.chassisnumber)
#       instance.price = validated_data.get('price' , instance.price)
#       instance.save()
#       return instance
  
  # Field level validators (for price)
  def validate_price(self, value):
      if value <= 20000.00:
          raise serializers.ValidationError("Price must be greater than 20000.00")
      return value
  


  

  
   

      


# Object level validation
  def validate(self, data):
       if data['name'] == data['description']:
           raise serializers.ValidationError("Name and Description must be different")
       return data
  
  
  





  # Purpose of this serializers is to convert
  # Complex json into Python dictionary
