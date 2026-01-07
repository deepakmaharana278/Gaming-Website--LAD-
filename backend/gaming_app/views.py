from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


@api_view(['POST'])
def register(req):
    user_name = req.data.get('user_name')
    email = req.data.get('email')
    password = req.data.get('password')

    if User.objects.filter(email=email).exists():
        return Response({"message":"Email already registered"},status=400)
    User.objects.create(user_name=user_name,email=email,password=make_password(password))
    return Response({"message":"User Registered Successfully"},status=201)

