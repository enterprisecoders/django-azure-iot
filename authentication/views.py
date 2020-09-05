from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class SessionProvider(APIView):

    def post(self, request, format=None):
        
