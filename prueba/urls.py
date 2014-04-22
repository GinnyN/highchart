from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()
from graphic import views
from tastypie.api import Api
from graphic import resources

v1_api = Api(api_name='v1')
v1_api.register(resources.JugoResource())

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.Root.as_view(), name='root'),
    url(r'^upload/', views.Upload.as_view(), name='upload'),
    url(r'^api/', include(v1_api.urls)),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
