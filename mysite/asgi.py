# import django
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.core.asgi import get_asgi_application
# from app.consumers import ChatConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# これが必要らしい
# django.setup()
django_asgi_app = get_asgi_application()

from app.consumers import ChatConsumer


# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.


# from chat.consumers import AdminChatConsumer, PublicChatConsumer

application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": django_asgi_app,
    # "http": get_asgi_application(),

    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^ws/chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi()),
        ])
    ),
})
