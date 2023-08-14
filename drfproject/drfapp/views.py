from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drfapp.serializers import StudentSerializer
from drfapp.models import Student

class GetCreate(APIView):
    def get(self, request, *args, **Kwargs):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True )
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
class GetUpdateDelete(APIView):
    def get(self, request, id, *args, **kwargs ):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self, request, id,  *args, **kwargs):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)