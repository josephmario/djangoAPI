import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins
# Create your views here.

class PersonList(generics.GenericAPIView, mixins.ListModelMixin, 
                 mixins.CreateModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class PersonDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)


'''
class PersonList(APIView):

    # def get_object(self, id):
    #     try:
    #        return Person.objects.get(id = id)
    #     except Person.DoesNotExist:
    #         return HttpResponse(status=status.HTTP_404_NOT_FOUND)


    def get(self, request):
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
        # person = self.get_object(id)
        # serializer = PersonSerializer(person)
        # return Response(serializer.data)


    def put(self, request, id):
        person = self.get_object(id)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        person = self.get_object(id)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PersonDetails(APIView):

    def get_object(self, id):
        try:
           return Person.objects.get(id = id)
        except Person.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)


    def get(self, request, id):
        person = self.get_object(id)
        serializer = PersonSerializer(person)
        return Response(serializer.data)


    def put(self, request, id):
        person = self.get_object(id)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        person = self.get_object(id)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
'''
@api_view(['GET', 'POST'])
def person_list(request):

    if request.method == 'GET':
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400) 

@api_view(['GET', 'PUT', 'DELETE'])
def person_details(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return HttpResponse(statue=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        person.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
'''