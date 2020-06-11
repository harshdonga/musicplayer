from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('',views.index, name = 'index'),
    path('upload', views.upload, name = 'upload'),
    path('post', views.post, name = 'post')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)