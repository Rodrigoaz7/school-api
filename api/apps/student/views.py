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

class StudentView(APIView):

    serializer_class = StudentSerializer
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(responses={200: StudentSerializer(many=True)}, manual_parameters=getSwaggerParams())
    def get(self, request):
        filters = getFiltersRequest(request.GET)
        ordering = getOrderingRequest(request.GET)
        students = utils.genericQuery(Student, filters, ordering)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={201: StudentSerializer(many=False)}, request_body=StudentPersistSerializer(many=False))
    def post(self, request):
        try:
            serializer = StudentPersistSerializer(data=request.data, many=False)
            serializer.is_valid(raise_exception=True)
            savedObj = serializer.create()
            serializer = StudentSerializer(savedObj, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):

    serializer_class = StudentSerializer
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(responses={200: StudentSerializer(many=False)})
    def get(self, request, pk, format=None):
        student = utils.getObject(Student, pk)
        if not student:
            return Response('Student does not exist', status=status.HTTP_204_NO_CONTENT)
        serializer = StudentSerializer(student, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={200: StudentSerializer(many=False)}, request_body=StudentPersistSerializer(many=False))
    def put(self, request, pk, format=None):
        student = utils.getObject(Student, pk)
        if not student:
            return Response('Student does not exist', status=status.HTTP_204_NO_CONTENT)
        try:
            data = StudentForm(request.data, False).form
            objSaved = utils.updateObject(Student, student, data)
            serializer = StudentSerializer(objSaved, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={200: StudentSerializer(many=False)}, request_body=StudentPersistSerializer(many=False))
    def patch(self, request, pk, format=None):
        student = utils.getObject(Student, pk)
        if not student:
            return Response('Student does not exist', status=status.HTTP_204_NO_CONTENT)
        try:
            data = StudentForm(request.data, False).form
            objSaved = utils.updateObject(Student, student, data)
            serializer = StudentSerializer(objSaved, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'Message of success'})
    def delete(self, request, pk, format=None):
        student = utils.getObject(Student, pk)
        if not student:
            return Response('Student does not exist', status=status.HTTP_400_BAD_REQUEST)
        student.delete()
        return Response('Student deleted', status=status.HTTP_204_NO_CONTENT)