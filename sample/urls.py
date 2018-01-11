from django.conf.urls import url

from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    # 127.0.0.1:8000/sample/publish でメッセージを送れるようにする
    url(r'^publish$', views.publish, name='publish'),
]
