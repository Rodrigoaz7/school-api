from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from rest_framework.generics import *
from django.core.exceptions import *
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import permission_classes
from utils import general as utils
from .params import getSwaggerParams, getFiltersRequest, getOrderingRequest
from .forms import StudentForm
from .models import Class

class ClassView(APIView):

    serializer_class = ClassSerializer
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(responses={200: ClassSerializer(many=True)}, manual_parameters=getSwaggerParams())
    def get(self, request):
        filters = getFiltersRequest(request.GET)
        ordering = getOrderingRequest(request.GET)
        classes = utils.genericQuery(Class, filters, ordering)
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={201: ClassSerializer(many=False)}, request_body=ClassPersistSerializer(many=False))
    def post(self, request):
        try:
            serializer = ClassPersistSerializer(data=request.data, many=False)
            serializer.is_valid(raise_exception=True)
            savedObj = serializer.create()
            serializer = ClassSerializer(savedObj, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


class ClassDetailView(APIView):

    serializer_class = ClassSerializer
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(responses={200: ClassSerializer(many=False)})
    def get(self, request, pk, format=None):
        schoolClass = utils.getObject(Class, pk)
        if not schoolClass:
            return Response('Class does not exist', status=status.HTTP_204_NO_CONTENT)
        serializer = ClassSerializer(schoolClass, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={200: ClassSerializer(many=False)}, request_body=ClassPersistSerializer(many=False))
    def put(self, request, pk, format=None):
        schoolClass = utils.getObject(Class, pk)
        if not schoolClass:
            return Response('Class does not exist', status=status.HTTP_204_NO_CONTENT)
        try:
            data = StudentForm(request.data, False).form
            objSaved = utils.updateObject(Class, schoolClass, data)
            serializer = ClassSerializer(objSaved, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={200: ClassSerializer(many=False)}, request_body=ClassPersistSerializer(many=False))
    def patch(self, request, pk, format=None):
        schoolClass = utils.getObject(Class, pk)
        if not schoolClass:
            return Response('Class does not exist', status=status.HTTP_204_NO_CONTENT)
        try:
            data = StudentForm(request.data, False).form
            objSaved = utils.updateObject(Class, schoolClass, data)
            serializer = ClassSerializer(objSaved, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'Message of success'})
    def delete(self, request, pk, format=None):
        schoolClass = utils.getObject(Class, pk)
        if not schoolClass:
            return Response('Class does not exist', status=status.HTTP_400_BAD_REQUEST)
        schoolClass.delete()
        return Response('Class deleted', status=status.HTTP_204_NO_CONTENT)