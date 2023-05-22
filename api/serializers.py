import re

from django.http import HttpResponse
from rest_framework import serializers

from api.models import user


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=['id','name','email','phone','dob']

    def validate(self,data):
        mno=str(data.get('phone'))
        if mno is not None:
            number=re.match('(9|8|7)',mno)
            if number is None:
                raise serializers.ValidationError("incorect number it should be start from 9 or 8 or 7")
            return data
        return HttpResponse("number not found ")