from django.shortcuts import render, redirect
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User

def index(request):
    #return redirect('/swagger/')
    return render(request, "accounts/index.html")

@api_view(['GET'])
def user_list(request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)

