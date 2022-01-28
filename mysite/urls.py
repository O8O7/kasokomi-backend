from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/auth/', include('accounts.urls')),
    path('api/app/', include('app.urls')),
    path('admin/', admin.site.urls),
]

# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT
#     )
# urlpatterns += static(
#     settings.MEDIA_URL,
#     document_root=settings.MEDIA_ROOT
# )

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG == False:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
#         static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 開発用

# if settings.DEBUG == False:
#     from django.urls import re_path
#     from django.views.static import serve
#     urlpatterns += [
#         re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
#         re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
#     ]
