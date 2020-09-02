from django.conf.urls import include, url
from django.contrib import admin
from apps.frontend import urls as f_url
from django.conf.urls.i18n import i18n_patterns
from apps.frontend.views import HomeView, AboutUsView, ServicesView

urlpatterns =  [

    # Examples:
    # url(r'^$', 'cabs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^', include(f_url)),
    url(r'^', include('apps.frontend.urls')),
    # url(r'^', include(f_url))
    url(r'^employee/', include('apps.employee.urls')),
]

