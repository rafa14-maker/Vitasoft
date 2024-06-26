# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import User
# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# from .serializers import SignUpSerializer, UserSerializer


# @api_view(["POST"])
# def register(request):
#     data = request.data

#     user = SignUpSerializer(data=data)

#     if user.is_valid():
#         user = User.objects.create(
#             first_name=data["first_name"],
#             last_name=data["last_name"],
#             email=data["email"],
#             username=data["email"],
#             password=make_password(data["password"]),
#         )

#         return Response({"details": "User Registered"}, status=status.HTTP_201_CREATED)
#     else:
#         return Response(user.errors)

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (
    SignUpSerializer,
    UserLoginSerializer,
    UserProfileUpdateSerializer,
    UserSerializer,
)


@api_view(["POST"])
def register(request):
    data = request.data
    serializer = SignUpSerializer(data=data)
    if serializer.is_valid():
        user = User.objects.create_user(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            username=data["email"],
            password=data["password"],
        )
        return Response({"details": "User Registered"}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login_user(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return Response({"details": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT", "PATCH"])
def update_user_profile(request):
    user = request.user
    serializer = UserProfileUpdateSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_user_profile(request):
    user = request.user
    user.delete()
    return Response({"details": "User deleted"}, status=status.HTTP_204_NO_CONTENT)
