from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import user
from api.serializers import userSerializer


# Create your views here.


def home(request):
    return render(request,'home.html')


@method_decorator(csrf_exempt,name='dispatch')
class register(APIView):
    def post(self,request):
        data=request.data
        mail=data.get('email')
        serializer=userSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                "Registration Sucessfull",
                "Congratulations you have successfully register with us",
                "2018pcemerohit58@poornima.org",
                ['"' + mail + '"'],
                fail_silently=False,
            )
            oldData=user.objects.all()
            serializer1=userSerializer(oldData, many=True)
            details={'olddata':serializer1.data}
            return render(request,'all.html',details)
        return Response(serializer.errors)
