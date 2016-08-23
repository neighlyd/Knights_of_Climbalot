from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.edit_session, name='edit_session'),
    url(r'^new/$', views.new_session, name='new_session')
]
