from django.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter

from app.views import PostViewSet

routers = SimpleRouter()
routers.register('post', PostViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
