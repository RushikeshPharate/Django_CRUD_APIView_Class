from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student
from rest_framework import status
from .serializers import StudentSerializer
# Create your views here.

class StudentAPI(APIView):

    def get(self,request,pk=None,format=None):
        try:
            id = request.data.get('id',None)
            if id is not None:
                print("Inside")
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data,status=status.HTTP_200_OK)
            stu = Student.objects.all()
            serializer = StudentSerializer(stu,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"msg":"Something went wrong"},status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serialzer = StudentSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response({"msg":"Data Posted"},status=status.HTTP_201_CREATED)
        return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,format=None):
        try: 
            id = request.data.get("id")
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Full/PUT Update Successfull"},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"msg":"Something went wrong"},status=status.HTTP_404_NOT_FOUND)

    def patch(self,request,format=None):
        try:
            id = request.data.get("id")
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Partial/PATCH Update Successfull"},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"msg":"Something went wrong"},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,format=None):
        try: 
            id = request.data.get("id")
            stu = Student.objects.get(id=id)
            if stu:
                stu.delete()
                return Response({"msg":"Record Deleted Successfully"},status=status.HTTP_200_OK)
            return Response({"msg":"Something went wrong"},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"msg":"Something went wrong"},status=status.HTTP_404_NOT_FOUND)
                


