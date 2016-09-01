from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from climbalot.models import *
from rest_framework import permissions, viewsets, generics, status
from climbalot.serializers import *
from climbalot.permissions import IsUserOrReadOnly, IsMonkeyOrReadOnly
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

"""
View Classes for drf-Nested-Routers. This provides an easy way to make a string of nested urls
to refer to the API. However, dealing with permissions and saving becomes a nightmare that I haven't been
able to figure out.
"""

class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    def list(self, request,):
        queryset = User.objects.filter()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.filter()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class MonkeyViewSet(viewsets.ModelViewSet):
    serializer_class = MonkeySerializer
    queryset = Monkey.objects.filter()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(player=self.request.user)

    def list(self, request, user_pk=None, monkey_pk=None):
        queryset = Monkey.objects.get(player=user_pk)
        serializer = MonkeySerializer(queryset, many=False)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_pk=None):
        queryset = Monkey.objects.filter(pk=pk, player=user_pk)
        monkey = get_object_or_404(queryset, pk=pk)
        serializer = MonkeySerializer(monkey)
        return Response(serializer.data)

class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects.filter()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsMonkeyOrReadOnly)

    def list(self, request, user_pk=None, monkey_pk=None):
        queryset = Session.objects.filter(monkey__player=user_pk, monkey=monkey_pk)
        serializer = SessionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_pk=None, monkey_pk=None):
        queryset = Session.objects.filter(pk=pk, monkey=monkey_pk, monkey__player=user_pk)
        session = get_object_or_404(queryset, pk=pk)
        serializer = SessionSerializer(session)
        return Response(serializer.data)


class QuestViewSet(viewsets.ModelViewSet):
    serializer_class = QuestSerializer
    queryset = Quest.objects.filter()

    def list(self, request, user_pk=None, monkey_pk=None, status=None):
        if status is not None:
            status = status[0]
            status.upper()
            queryset = Quest.objects.filter(status=status, monkey__player=user_pk, monkey=monkey_pk)
        else:
            queryset = Quest.objects.filter(monkey__player=user_pk, monkey=monkey_pk)
        serializer = QuestSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_pk=None, monkey_pk=None, status=None):
        if status is not None:
            status = status[0]
            status.upper()
            queryset = Quest.objects.filter(pk=pk, monkey=monkey_pk, monkey__player=user_pk)
        queryset = Quest.objects.filter(pk=pk, monkey=monkey_pk)
        quest = get_object_or_404(queryset, pk=pk)
        serializer = QuestSerializer(quest)
        return Response(serializer.data)

class C_RoutesViewSet(viewsets.ModelViewSet):
    serializer_class = C_RoutesSerializer
    queryset = C_Routes.objects.filter()

    def list(self, request, user_pk=None, monkey_pk=None, session_pk=None):
        queryset = C_Routes.objects.filter(id=session_pk)
        serializer = C_RoutesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_pk=None, monkey_pk=None, session_pk=None):
        queryset = C_Routes.objects.filter(pk=pk, session__monkey=monkey_pk, session__monkey__player=user_pk, session=session_pk)
        quest = get_object_or_404(queryset, pk=pk)
        serializer = C_RoutesSerializer(quest)
        return Response(serializer.data)

class V_RoutesViewSet(viewsets.ModelViewSet):
    serializer_class = V_RoutesSerializer
    queryset = V_Routes.objects.filter()

    def list(self, request, user_pk=None, monkey_pk=None, session_pk=None):
        queryset = V_Routes.objects.filter(id=session_pk)
        serializer = V_RoutesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_pk=None, monkey_pk=None, session_pk=None):
        queryset = V_Routes.objects.filter(pk=pk, session__monkey=monkey_pk, session__monkey__player=user_pk, session=session_pk)
        quest = get_object_or_404(queryset, pk=pk)
        serializer = V_RoutesSerializer(quest)
        return Response(serializer.data)

class Y_RoutesViewSet(viewsets.ModelViewSet):
    serializer_class = Y_RoutesSerializer
    queryset = Y_Routes.objects.filter()

    def list(self, request, user_pk=None, monkey_pk=None, session_pk=None):
        queryset = Y_Routes.objects.filter(id=session_pk)
        serializer = Y_RoutesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_pk=None, monkey_pk=None, session_pk=None):
        queryset = Y_Routes.objects.filter(pk=pk, session__monkey=monkey_pk, session__monkey__player=user_pk, session=session_pk)
        quest = get_object_or_404(queryset, pk=pk)
        serializer = Y_RoutesSerializer(quest)
        return Response(serializer.data)

"""
These Views auto-include CRUD operations, but are more difficult to send **kwargs to for
dynamic filtering.
"""
"""
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_pk'

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
"""
