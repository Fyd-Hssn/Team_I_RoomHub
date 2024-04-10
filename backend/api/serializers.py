from rest_framework import serializers
# from .models import Products
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserProfile, Listing


class UserSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField(read_only=True)
    _id=serializers.SerializerMethodField(read_only=True)
    isAdmin=serializers.SerializerMethodField(read_only=True)
   
    class Meta:
        model=User
        fields=['id','_id','username','email','name','isAdmin']
    
    def get_name(self,obj):
        firstname=obj.first_name
        lastname=obj.last_name
        name=firstname+' '+lastname
        if name=='':
            name=obj.email[:5]
            return name
        return name
    
    def get__id(self,obj):
        return obj.id

    def get_isAdmin(self,obj):
        return obj.is_staff


class UserSerializerWithToken(UserSerializer):
    token=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        fields=['id','_id','username','email','name','isAdmin','token']
    
    def get_token(self,obj):
        token=RefreshToken.for_user(obj)
        return str(token.access_token)

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields = [
            'user',
            'first_name',
            'last_name',
            'profile_picture',
            'bio',
            'age',
            'gender',
            'school',
            'pets',
            'allergies',
            'budget',
            'sleep_schedule'
        ]

