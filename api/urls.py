from django.conf.urls import url, include
from api import views
from rest_framework_nested import routers

"""
Routers for drf-Nested-Routers schema.
"""
router=routers.SimpleRouter()
router.register(r'users', views.UserViewSet, base_name='users')

user_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
user_router.register(r'monkeys', views.MonkeyViewSet, base_name='monkeys')

monkey_router = routers.NestedSimpleRouter(user_router, r'monkeys', lookup='monkey')
monkey_router.register(r'sessions', views.SessionViewSet, base_name='sessions')
monkey_router.register(r'quests', views.QuestViewSet, base_name='quests')
monkey_router.register(r'quests.(?P<status>(?i)active|completed|failed)', views.QuestViewSet, base_name='quest_status')

session_router = routers.NestedSimpleRouter(monkey_router, r'sessions', lookup='session')
session_router.register(r'c_route', views.C_RoutesViewSet, base_name='c_route')
session_router.register(r'v_route', views.V_RoutesViewSet, base_name='v_route')
session_router.register(r'y_route', views.Y_RoutesViewSet, base_name='y_route')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(user_router.urls)),
    url(r'^', include(monkey_router.urls)),
    url(r'^', include(session_router.urls))
]


"""
URLs for regular REST framework schema.
Rather than using routers, I explicitly set up the URL paths using regex hooks to grab variables to feed into the views.
"""
"""
urlpatterns = [
    url(r'^users', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<user_pk>\d+)$', views.UserDetail.as_view(), name='user-detail')
]
"""
