# from django.http import HttpResponse
from django.http.response import JsonResponse
import json

class Const():
    @staticmethod
    def toOkResult(msg):
        msg = { "status" : str(StatusCode.ok),
                # "contents" : json.dumps(msg_dict),
                "contents" : msg,
        }
        response = JsonResponse(msg)
        response = Const.add_cors_allow(response)
        return response


    @staticmethod
    def add_cors_allow(response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response


class StatusCode():
    ok = 200
