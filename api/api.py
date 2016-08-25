from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from climbalot import views as climbalot_views

urlpatterns = [
    url(r'^monkeys/$', climbalot_views.MonkeyList.as_view()),
    url(r'^monkeys/(?P<pk>\d+)/$', climbalot_views.MonkeyDetail.as_view()),
    url(r'users/$', climbalot_views.UserList.as_view()),
    url(r'users/(?P<pk>\d+)/$', climbalot_views.UserDetail.as_view()),
    url(r'sessions/$', climbalot_views.SessionList.as_view()),
    url(r'sessions/(?P<pk>\d+)/$', climbalot_views.SessionDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
