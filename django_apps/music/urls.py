from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.MusicListCreateView.as_view()),
    url(r"^playlist/$", views.PlaylistListCreateView.as_view(), ),
    url(r'^(?P<pk>\d+)/$', views.MusicRetrieveView.as_view()),
]
