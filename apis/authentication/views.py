from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models

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

    new_doctor = models.Doctor_Authentication(
        email=request.data['email'],
        password=request.data['password'],
        name=request.data['name'],
        phone=request.data['phone'],
        address=request.data['address'],
        specialization=request.data['specialization'],
        experience=request.data['experience'],
        qualifications=request.data['qualifications'],
        about=request.data['about'],
    )
    new_doctor.save()     
    return Response('User Created!', status=200)

@api_view(['POST'])
def checkDoctor(request) -> Response:
    if doctorExists(request.data['email'], request.data['password']) == True:
        return Response('User Already Exist!')
    return Response('User doesn\'t exist')

@api_view(['DELETE'])
def deleteDoctor(request) -> Response:
    if doctorExists(request.data['email'], request.data['password']) == False:
        return Response('User doesn\'t exist')

    models.Doctor_Authentication.objects.get(email = request.data['email'], password = request.data['password']).delete()
    return Response('User Deleted', status=200)