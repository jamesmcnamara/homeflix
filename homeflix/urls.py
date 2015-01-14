from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.routers import DefaultRouter
from videos.views import HomePage, VideoViewSet


router = DefaultRouter()
router.register(r"^videos", VideoViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homeflix.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomePage.as_view(), name="home"),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()