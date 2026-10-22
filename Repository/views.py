from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from Repository.models import Questions
from Repository.models import submission
from Repository.serializers import QuestionSereializer
from Repository.serializers import SubmissionSerializer
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
        qs=get_object_or_404(submission,id=pk)
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

    def delete(self,request,pk):
          Questions.objects.filter(id=pk).delete()
          return Response(data={"message":"question deleted successfully"})

class SubmissionListCreateView(APIView):
    def get(self,request):
        qs=submission.objects.all()
        serializer_instance=SubmissionSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    
    def post(self,request):#create
        form_data=request.data  #form_data dictionary->python native type
        serializer_instance=SubmissionSerializer(data=form_data)#create serializer_instance with form_data
        if serializer_instance.is_valid(): #check the data is valid according to the seriolizer's validation rule
            actual_data=serializer_instance.validated_data #get the validated data from the serializer
            submission.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class SubmissionRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):
        qs=submission.objects.get(id=pk)
        serializer_instance=SubmissionSerializer(qs)
        return Response(data=serializer_instance.data)
    def put(self,request,pk):#create
        form_data=request.data  #form_data dictionary->python native type
        serializer_instance=SubmissionSerializer(data=form_data)#create serializer_instance with form_data
        if serializer_instance.is_valid(): #check the data is valid according to the seriolizer's validation rule
            actual_data=serializer_instance.validated_data #get the validated data from the serializer
            submission.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        submission.objects.filter(id=pk).delete()
        return Response(data={"message":" deleted successfully"})

class EvaluatesubmissionView(APIView):
    def put(self,request,pk):
        form_data=request.data
        submission.objects.filter(id=pk).update(**form_data)
        return Response(data={
            "message":"updated...!"
        })
