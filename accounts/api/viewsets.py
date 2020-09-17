from accounts.models import User
from accounts.api.serializers import UserSerializer, UserPrintSerializer
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin):
    # list, create, retrieve, update, partial_update, destroy

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        newest = self.get_queryset()
        serializer = UserPrintSerializer(newest, many=True)
        return Response(serializer.data)
