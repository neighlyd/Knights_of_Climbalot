from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views



# Users URL patterns

user_urls = [
    url(r'^$', views.UserList.as_view(), name='user-list'),
    url(r'^(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user-detail')
]

monkey_urls = [
    url(r'^$', views.MonkeyList.as_view(), name='monkey-list'),
    url(r'^(?P<pk>\d+)/$', views.MonkeyDetail.as_view(), name='monkey-detail'),
    url(r'^(?P<pk>\d+)/sessions', views.MonkeySessionList.as_view(), name='monkeysession-list'),
    url(r'^(P<pk>\d+)/quests', views.QuestList.as_view(), name='monkeyquest-list')
]

session_urls = [
    url(r'^$', views.SessionList.as_view(), name='session-list'),
    url(r'^(?P<pk>\d+)/$', views.SessionDetail.as_view(), name='session-detail'),
    url(r'^(?P<pk>\d+)/c_routes/$', views.SessionCRouteDetail.as_view(), name='session_c_route-detail'),
    url(r'^(?P<pk>\d+)/v_routes/$', views.SessionVRouteDetail.as_view(), name='session_v_route-detail'),
    url(r'^(?P<pk>\d+)/y_routes/$', views.SessionYRouteDetail.as_view(), name='session_y_route-detail')
]

quest_urls = [
    url(r'^$', views.QuestList.as_view(), name='quest-list'),
    url(r'^status/(?P<status>[ACF])/$', views.QuestListStatus.as_view(), name='quest-status-list')
]

urlpatterns = [
    #url(r'^', include(router.urls)),
    url(r'users/', include(user_urls)),
    url(r'monkeys/', include(monkey_urls)),
    url(r'sessions/', include(session_urls)),
    url(r'quests/', include(quest_urls))
    #url(r'(?P<pk>\d+)/sessions$', views.MonkeySessionList.as_view(), name='monkeysessions-list'),
    #url(r'sessions/(?P<pk>\d+)/c_routes$', views.C_RoutesViewSet.as_view({'get':'list'}), name='sessioncroute-detail')
    #url(r'sessions/$', views.SessionList.as_view(), name='sessions-list'),
    #url(r'sessions/(?P<pk>\d+)/$', views.SessionDetail.as_view(), name='sessions-detail')
]

#urlpatterns = format_suffix_patterns(urlpatterns)
