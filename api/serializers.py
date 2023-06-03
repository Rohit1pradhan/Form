import re

from django.http import HttpResponse
from rest_framework import serializers
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','name','email','phone','dob']

    def validate(self, data):
        mno = str(data.get('phone'))
        if mno is not None:
            number = re.match('(9|8|7)', mno)
            if number is None:
                raise serializers.ValidationError("incorect number it should be start from 9 or 8 or 7")
            return data
        return HttpResponse("number not found ")
class userserializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model=User
        fields=['email','name','dob','phone','password','password2',]
        extra_kwargs={
            'password':{'write_only':True}
        }
    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        print(password,password2)
        if password!=password2:
            raise serializers.ValidationError("password and conform doesn't match")
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class userLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']