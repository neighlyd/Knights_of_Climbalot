from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from climbalot import views

index_urls = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$', views.home_files, name="home-files"),

]

session_urls =[
    url(r'^$', login_required(views.AllSessionList.as_view()), name='view-all-sessions'),
    url(r'^new/$', views.new_session, name='new-session'),
    url(r'^(?P<session_pk>\d+)/$', views.edit_session),
]

monkey_urls = [
    url(r'create/', views.create_monkey, name='create-monkey'),
    url(r'(?P<monkey_pk>\d+)/$', views.monkey, name='monkey-home'),
    url(r'(?P<monkey_pk>\d+)/sessions/', include(session_urls)),
]

urlpatterns = [
    url(r'', include(index_urls)),
    #url(r'', login_required(views.AllSessionList.as_view())),
    url(r'^monkey/', include(monkey_urls))
]
