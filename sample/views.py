from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http.response import JsonResponse

from channels import Group
import json

from . import consumers
from . import Const


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
    Group("sample").send({"text": json.dumps({"x": x,"y": y})})
    print(x,y)
    return HttpResponse("Published!")


def get_data(request):
    pass



"""
以下API
"""

from sample.script.RunPython import RunPython
learning = RunPython("loop.py")
kafka_mes_ws = RunPython("send_req.py")


def start_learing(request):
    status_msg = learning.start()
    return Const.Const().toOkResult({"learning" : status_msg})


def stop_learing(request):
    learning.stop()
    return Const.Const().toOkResult({"learning" : "stop"})


def get_pid(request):
    pid = learning.get_pid()
    if pid == "" :
        msg = {"pid":"none"}
    else :
        msg = {"pid":str(pid)}
    return Const.Const().toOkResult(msg)


def start_kafka_cons(request):
    status_msg = kafka_mes_ws.start()
    return Const.Const().toOkResult({"learning" : status_msg})


def stop_kafka_cons(request):
    kafka_mes_ws.stop()
    return Const.Const().toOkResult({"learning" : "stop"})


def get_kafka_cons_pid(request):
    pid = kafka_mes_ws.get_pid()

    if pid == "" :
        msg = { "pid" : "none" }
    else :
        msg = { "pid" : str(pid) }
    return Const.Const().toOkResult(msg)
