from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sessions/(^P<pk>\d+)/$', views.session, name='session_view'),
]
