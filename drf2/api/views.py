from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from api.serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def student_create(req):
    if req.method == 'POST':
        json_data = req.body
        stream = io.BytesIO(json_data) # Convert JSON data to stream data
        py_data = JSONParser().parse(stream) # Convert stream data to python data
        serializer = StudentSerializer(data=py_data) # Convert python data to serializer(Complex data type)
        if serializer.is_valid(): # Check if serializer data is valid or not
            serializer.save() # Save data to database
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res) # Convert res data to JSON data
            return HttpResponse(json_data, content_type='application/json')
            # return JsonResponse(res, safe=False)

        json_data = JSONRenderer().render(serializer.errors) # Convert serializer data to JSON data
        return HttpResponse(json_data, content_type='application/json')