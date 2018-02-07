# import kafka
from kafka import KafkaConsumer
import requests
from websocket import create_connection
from time import sleep
import json


class WsCons():
    IP="127.0.0.1"
    PORT="8000"
    URI="/REST_PUB"

class KafkaConsumerCons():
    PORT="9092"
    TOPIC='makesentens'
    IP1="35.194.228.2"
    IP2="45.76.199.23"


def send_message(consumer):
    for message in consumer:
        print("topic: %s message=%s" % (message.topic, message.value))
        url="http://" + WsCons.IP + ":" + WsCons.PORT + WsCons.URI + "?x=" + message.value['x'] + "&y=" + message.value['y']
        resp = requests.get(url)


def test():
    import random as rand

    for i in range(10000):
        send = str(rand.randint(0,10)/10)
        print("send "+send)
        url = "http://" + WsCons.IP + ":" + WsCons.PORT + URI + "?x=" + str(i) + "&y=" + send
        resp = requests.get(url)
        sleep(0.5)


def main():
    host1 = KafkaConsumerCons.IP1 + ':' + KafkaConsumerCons.PORT
    host2 = KafkaConsumerCons.IP2 + ':' + KafkaConsumerCons.PORT
    consumer = KafkaConsumer(KafkaConsumerCons.TOPIC,
                             bootstrap_servers=[host1, host2],
                             # auto_offset_reset='earliest',
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')))
                             # value_deserializer=lambda m: json.loads(m).decode('utf-8'))

    send_message(consumer)



if __name__ == "__main__":
    # main()
    test()

