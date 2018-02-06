from channels import Group
import json
import re

GROUP="sample"

def check_data_format(data):
    __data = data
    patern = 'x=([+-]?[0-9]+\.?[0-9]*),y=([+-]?[0-9]+\.?[0-9]*)'
    # print(data)
    return bool(re.compile(patern).match(__data))


def get_xy(data):
    x_data = data.split(",")[0]
    y_data = data.split(",")[1]

    x = x_data.split("=")[1]
    y = y_data.split("=")[1]
    return x, y


def ws_message(message):
    data = message.content['text']
    print(data)
    if check_data_format(data):
        x, y = get_xy(data)
        Group(GROUP).send({"text": json.dumps({"x": x, "y": y }) })


def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group(GROUP).add(message.reply_channel)


def ws_disconnect(message):
    Group(GROUP).discard(message.reply_channel)
