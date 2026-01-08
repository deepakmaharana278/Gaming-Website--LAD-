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
    return Response({"message":"Account created successfully"},status=201)

@api_view(['POST'])
def login(req):
    email = req.data.get('email')
    password = req.data.get('password')

    try:
        user = User.objects.get(email=email)
        if check_password(password,user.password):
            return Response({"message":"Login Successfully"},status=200)
        else:
            return Response({"message":"Invalid Creadential"},status=401)
    except:
        return Response({"message":"User not found"},status=404)