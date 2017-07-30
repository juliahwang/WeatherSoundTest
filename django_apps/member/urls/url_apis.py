from django.conf.urls import url

from .. import views

urlpatterns = [
    url(r'^$', views.UserListCreateView.as_view()),
    url(r'^(?P<pk>\d+)/$', views.UserRetrieveUpdateDestroyView.as_view()),

]
