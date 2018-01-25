from django.conf.urls import url

from . import views
from django.urls import path, include

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^result/$', views.result, name='result'),
    url(r'^glaph/$', views.glaph, name='glaph'),
    url(r'^start/$', views.start_learing, name='start'),
    url(r'^stop/$', views.stop_learing, name='stop'),
    url(r'^progress/$', views.get_pid, name='progress'),
    # 127.0.0.1:8000/sample/publish でメッセージを送れるようにする
    url(r'^publish$', views.publish, name='publish'),
]
