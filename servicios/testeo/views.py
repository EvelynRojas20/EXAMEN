from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from logica import users
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# Create your views here.
def index(request):
    nick_name=request.POST.get('nick_name')
    description=request.POST.get('description')
    try:
        user= users.create_user(nick_name=nick_name,description=description)
        response={
        "status":"sucessfull",
        "code":200,
        "data":"Listo"
    }
    except Exception as err:
            response={
        "status":"error",
        "code":500,
        "data":str(err)
    }
    return JsonResponse(response)