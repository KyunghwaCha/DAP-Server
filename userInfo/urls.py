from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    #url(r'^$', views.user_list.as_view()),
    #url(r'^(?P<pk>[0-9]+)/$', views.user_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)