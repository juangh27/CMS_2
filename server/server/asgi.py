"""
ASGI config for server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack 
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application


import cms.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')


application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websocket': AuthMiddlewareStack(  # new
        URLRouter(
          cms.routing.websocket_urlpatterns
        )
    ),  # new
})


# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": URLRouter([
#       path('practice', cms.consumers.PracticeConsumer.as_asgi())
# ])
# })

