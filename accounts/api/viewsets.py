from accounts.models import User
from accounts.api.serializers import UserSerializer
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin):
    # list, create, retrieve, update, partial_update, destroy

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('date_joined').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)
