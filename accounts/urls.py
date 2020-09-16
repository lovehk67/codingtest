from django.urls import path, include
from accounts.models import User
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'address_new', 'address_old', 'phone']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register('accounts', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]