import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def person_list(request):

    if request.method == 'GET':
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201) 
        return JsonResponse(serializer.errors, status=400) 


@csrf_exempt
def person_details(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return HttpResponse(statue=404)
    
    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PersonSerializer(person, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data) 
        return JsonResponse(serializer.errors, status=400) 
    
    elif request.method == 'DELETE':
        person.delete()
        return HttpResponse(status=204)