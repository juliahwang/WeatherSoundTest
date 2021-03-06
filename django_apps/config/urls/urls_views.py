"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render


def test_firstPage(request):
    return render(request, 'test/test.html')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^music/", include("music.urls")),
    url(r"^member/", include("member.urls.url_apis")),
    # url(r'^api/', include('snippets.urls')),
    # url(r'^__debug__/', include(debug_toolbar.urls)),

    url(r"^$", test_firstPage, name="first_page_test"),
]

# For Debugging
# TODO debugging일떄만 작동하도록l
urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
