from django.shortcuts import render
from rest_framework.response import Response
from Repository.models import Questions
from Repository.serializers import QuestionSereializer
from rest_framework.views import APIView
# Create your views here.

class QuestionlistView(APIView):
    def get(self,request):#fetch
        qs=Questions.objects.all()
        serializer_instance=QuestionSereializer(qs,many=True)
        return Response(serializer_instance.data)

    def post(self,request):#create
        form_data=request.data  #form_data dictionary->python native type
        serializer_instance=QuestionSereializer(data=form_data)#create serializer_instance with form_data
        if serializer_instance.is_valid(): #check the data is valid according to the seriolizer's validation rule
            actual_data=serializer_instance.validated_data #get the validated data from the serializer
            Questions.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class QuestionRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):# get one data 
        qs=Questions.objects.get(id=pk)
        serializer_instance=QuestionSereializer(qs)
        return Response(data=serializer_instance.data)
    def put(self,request,pk):
        form_data=request.data  #form_data dictionary->python native type
        serializer_instance=QuestionSereializer(data=form_data)#create serializer_instance with form_data
        if serializer_instance.is_valid(): #check the data is valid according to the seriolizer's validation rule
            actual_data=serializer_instance.validated_data #get the validated data from the serializer
            Questions.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)