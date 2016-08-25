from django.conf.urls import url, include
from climbalot import views


urlpatterns = [
    url(r'^new/$', views.new_session)
    url(r'/(?P<pk>\d+)/$', views.edit_session)
]
