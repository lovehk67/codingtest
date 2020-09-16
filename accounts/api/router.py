from accounts.api.viewsets import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('accounts', UserViewSet, basename='accounts')