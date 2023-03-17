from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


class ListViewSet(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    pass
