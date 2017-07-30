from django.conf.urls import url, include

urlpatterns = [
    url(r"^member/", include("member.urls.url_apis")),
    url(r"^music/", include("music.urls")), # TODO 패키지화

]
