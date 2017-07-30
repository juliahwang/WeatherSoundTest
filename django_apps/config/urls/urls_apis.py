from django.conf.urls import url, include

urlpatterns = [
    url(r"^member/", include("member.urls.url_apis")),
    url(r"^music/", include("music.urls")),  # TODO 패키지화

]
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
