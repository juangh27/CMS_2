from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    # re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'^ws/chat/(?P<room_name>help|questions|urgent)/$', consumers.ChatConsumer.as_asgi()),
    # re_path(r'ws/chat/help/$', consumers.ChatConsumer.as_asgi()),
    # re_path(r'ws/chat/questions/$', consumers.ChatConsumer.as_asgi()),
    # re_path(r'ws/chat/urgent/$', consumers.ChatConsumer.as_asgi()),
  
    # path("ws/chat/help/", consumers.ChatConsumer.as_asgi()),
    # path("ws/chat/questions/", consumers.ChatConsumer.as_asgi()),
    # path("ws/chat/urgent/", consumers.ChatConsumer.as_asgi()),
    # re_path(r'^ws/chat/help/$', consumers.ChatConsumer.as_asgi()),
    # re_path(r'^ws/chat/questions/$', consumers.ChatConsumer.as_asgi()),
    # re_path(r'^ws/chat/urgent/$', consumers.ChatConsumer.as_asgi()),
]       