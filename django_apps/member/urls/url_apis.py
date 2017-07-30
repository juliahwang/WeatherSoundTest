from django.conf.urls import url

from .. import views

urlpatterns = [
    url(r'^$', views.UserListCreateView.as_view()),
<<<<<<< HEAD
    url(r'^(?P<pk>\d+)/$', views.UserRetrieveUpdateDestroyView.as_view()),
=======
    # url(r'^(?P<pk>\d+)/$', apis.UserRetrieveUpdateDestroyView.as_view()),
>>>>>>> 5e21bf9c246b6a3e86a3f587d420a114c4936b18
]
