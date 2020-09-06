"""events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url

from django.urls import path, include
from django.contrib import admin


from . import views


urlpatterns = [

    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^events/', include('eventapi.urls')),
    url(r'^accounts/profile/(?P<pk>\d+)/(?P<username>[a-z0-9_-]+)/$', views.UserDetailView.as_view(), name='account_profile'),
    url(r'^accounts/profile/(?P<pk>\d+)/(?P<username>[a-z0-9_-]+)/edit/$', views.UserUpdateView.as_view(), name='account_profile_edit'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^inbox/notifications/', include('notifications.urls', namespace='notifications')),
]
