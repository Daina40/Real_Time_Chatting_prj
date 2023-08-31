from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/room_app/(?P<room>\w+)/$', ChatConsumer.as_asgi()),

]
