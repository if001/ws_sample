from django.conf.urls import url

from . import views
from django.urls import path, include

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^result/$', views.result, name='result'),
    url(r'^glaph/$', views.glaph, name='glaph'),

    url(r'^REST_START/$', views.start_learing, name='start'),
    url(r'^REST_STOP/$', views.stop_learing, name='stop'),
    url(r'^REST_PROCESS/$', views.get_pid, name='process'),


    url(r'^REST_START_KAFKA/$', views.start_kafka_cons, name='start_kafka'),
    url(r'^REST_STOP_KAFKA/$', views.stop_kafka_cons, name='stop_kafka'),
    url(r'^REST_KAFKA_PROCESS/$', views.get_kafka_cons_pid, name='process_kafka'),

    url(r'^REST_PUB$', views.publish, name='publish'),
]
