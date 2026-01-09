from django.urls import re_path
from .consumers import TelemedicinaConsumer

websocket_urlpatterns = [
    re_path(r"ws/telemedicina/(?P<sala>\w+)/$", TelemedicinaConsumer.as_asgi()),
]
