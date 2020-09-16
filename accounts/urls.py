from django.urls import path, include
from accounts.models import User
from rest_framework import routers, serializers, viewsets

from accounts import views

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'address_new', 'address_old', 'phone']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register('accounts', UserViewSet)


urlpatterns = [
    path('rest_api/', include(router.urls)),
    path('', views.index),
]