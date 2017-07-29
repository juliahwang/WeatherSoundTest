from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'api', views.SnippetViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

]
