from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from climbalot.models import *
from rest_framework import permissions, viewsets, generics
from climbalot.serializers import *
from climbalot.permissions import IsOwnerOrReadOnly, IsMonkeyOrReadOnly
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MonkeyList(generics.ListAPIView):
    queryset = Monkey.objects.all()
    serializer_class = MonkeySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class MonkeyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Monkey.objects.all()
    serializer_class = MonkeySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(player=self.request.user)

class SessionList(generics.ListAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(monkey=self.request.user.monkey)

#class SessionCRoutesList(generics.RetrieveUpdateDestroyAPIView):
#    queryset = C_Routes.objects.all()
#    serializer_class = C_RoutesSerializer
#    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsMonkeyOrReadOnly,)
#
#    def get_queryset(self):
#        queryset = super(SessionCRoutesViewSet, self).get_queryset()
#        return queryset.filter(session__pk=self.kwargs.get('pk'))

class SessionCRouteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = C_Routes.objects.all()
    serializer_class = C_RoutesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = super(SessionCRouteDetail, self).get_queryset()
        return queryset.filter(session__pk=self.kwargs.get('pk'))

class SessionVRouteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = V_Routes.objects.all()
    serializer_class = V_RoutesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = super(SessionVRouteDetail, self).get_queryset()
        return queryset.filter(session__pk=self.kwargs.get('pk'))

class SessionYRouteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Y_Routes.objects.all()
    serializer_class = Y_RoutesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = super(SessionYRouteDetail, self).get_queryset()
        return queryset.filter(session__pk=self.kwargs.get('pk'))


class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

class QuestList(generics.ListAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class QuestListStatus(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field="status"

    def get_queryset(self):
        queryset = super(QuestListStatus, self).get_queryset()
        return queryset.filter(status=self.kwargs.get('status'))

class QuestViewSet(viewsets.ModelViewSet):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class MonkeySessionList(generics.ListAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get_queryset(self):
        queryset = super(MonkeySessionList, self).get_queryset()
        return queryset.filter(monkey__pk=self.kwargs.get('pk'))
