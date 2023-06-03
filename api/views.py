from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import  User
from api.renderers import userRenderer
from api.serializers import userserializer, userLoginSerializer, UserSerializer


# Create your views here.


def home(request):
    return render(request,'home.html')


def loginpage(request):
    return render(request,'all.html')


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class userRegistrationView(APIView):
    renderer_classes = [userRenderer]
    def post(self,request):
        serializer=userserializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            mail=request.data.get('email')
            send_mail(
                'Registration Sucessfully',
                'congratulations you have registre sucessfully',
                '2018pcemerohit58@poornima.org',
                [mail],
                fail_silently=False,
            )
            token=get_tokens_for_user(user)
            olddata=User.objects.all()
            serializer1 = UserSerializer(olddata, many=True)
            details = {'olddata': serializer1.data}
            return Response({'msg':details},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class userLoginView(APIView):
    renderer_classes = [userRenderer]
    def post(self,request):
        serializer=userLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email,password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,"msg": "login Successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['email or password is not valid']}},status=status.HTTP_404_NOT_FOUND)
        else:
            Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

