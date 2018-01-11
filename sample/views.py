from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from channels import Group
import json

from . import consumers

def index(request):
    return render(request, 'sample/index.html')

def publish(request):
    x = request.GET.get('x', 'null')
    y = request.GET.get('y', 'null')
    Group("sample").send({"text": json.dumps({
        "x": x,
        "y": y
    })
    })
    print(x,y)
    return HttpResponse("Published!")
