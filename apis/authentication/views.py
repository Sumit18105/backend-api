from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializer
import os

# Create your views here.

def userExists(email: str, password: str):
    if models.User_Authentication.objects.filter(
        email = email,
        password = password
    ):
        return True
    return False


@api_view(['POST'])
def createUser(request) -> Response:
    if userExists(request.data['email'], request.data['password']) or models.User_Authentication.objects.filter(email = request.data['email']):
        return Response('User Already Exist!')

    new_user = models.User_Authentication(
        email=request.data['email'],
        password=request.data['password'],
        name=request.data['name'],
        phone=request.data['phone'],
        address=request.data['address'],
        pet_type=request.data['pet_type'],
    )
    new_user.save()     
    return Response('User Created!', status=200)

@api_view(['POST'])
def checkUser(request) -> Response:
    if userExists(request.data['email'], request.data['password']) == True:
        return Response('User Already Exist!')
    return Response('User doesn\'t exist')

@api_view(['DELETE'])
def deleteUser(request) -> Response:
    if userExists(request.data['email'], request.data['password']) == False:
        return Response('User doesn\'t exist')

    models.User_Authentication.objects.get(email = request.data['email'], password = request.data['password']).delete()
    return Response('User Deleted', status=200)
#For Doctor Authentication
def doctorExists(email: str, password: str):
    if models.Doctor_Authentication.objects.filter(
        email = email,
        password = password
    ):
        return True
    return False

@api_view(['POST'])
def createDoctor(request) -> Response:
    if doctorExists(request.data['email'], request.data['password']) or models.Doctor_Authentication.objects.filter(email = request.data['email']):
        return Response('User Already Exist!')
        
    doctor_serializer = serializer.Doctor_Authentication_Serializer(data = request.data)
    if doctor_serializer.is_valid():
        doctor_serializer.save()
    account_serializer = serializer.Accounts_Details_Serializer(data = request.data)
    if account_serializer.is_valid():
        account_serializer.save()
        return Response(doctor_serializer.data, status=200)
    else:return Response(doctor_serializer.errors or account_serializer.errors)

@api_view(['POST'])
def checkDoctor(request) -> Response:
    if doctorExists(request.data['email'], request.data['password']) == True:
        return Response('User Already Exist!')
    return Response('User doesn\'t exist')

@api_view(['DELETE'])
def deleteDoctor(request) -> Response:
    if doctorExists(request.data['email'], request.data['password']) == False:
        return Response('User doesn\'t exist')

    doctor = models.Doctor_Authentication.objects.get(email = request.data['email'], password = request.data['password'])
    try:os.remove(str(doctor.profile_picture))
    except:pass
    try:os.remove(str(doctor.qualifications_proof))
    except:pass
    try:os.remove(str(doctor.id_proof))
    except:pass
    doctor.delete()
    return Response('User Deleted', status=200)