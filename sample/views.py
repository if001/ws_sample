from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from channels import Group
import json

from . import consumers

def index(request):
    return render(request, 'sample/index.html')


def result(request):
    make = RunPython("make_sentence_test.py")
    print("pid:",make.get_pid())
    make.start()
    res = make.get_result()
    print(res)
    return render(request, 'sample/result.html')


def glaph(request):
    return render(request, 'sample/glaph.html')


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


def get_data(request):
    pass


from sample.script.RunPython import RunPython
learning = RunPython("loop.py")
kafka_mes_ws = RunPython("send_req.py")

def start_learing(request):
    status = learning.start()
    message = { "message" : status}
    return render(request, 'sample/learning.html',message)


def stop_learing(request):
    learning.stop()
    # return HttpResponse(stop)
    return render(request, 'sample/index.html')


def get_pid(request):
    pid = learning.get_pid()
    if pid == "" :
        message = {"message" : "実行されてません"}
    else :
        message = {"message" : "実行中です "+str(pid)}
    return render(request, 'sample/progress.html', message)


def start_kafka_cons(request):
    status = kafka_mes_ws.start()
    message = { "message" : status }
    return render(request, 'sample/learning.html',message)


def stop_kafka_cons(request):
    learning.stop()
    # return HttpResponse(stop)
    return render(request, 'sample/index.html')

