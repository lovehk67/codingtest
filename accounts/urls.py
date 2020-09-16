from django.urls import path, include
from accounts.models import User
from rest_framework import routers, viewsets
from .serializers import UserSerializer
from accounts import views

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register('accounts', UserViewSet)

urlpatterns = [
    path('rest_api/', include(router.urls)),
    path('', views.index),
]