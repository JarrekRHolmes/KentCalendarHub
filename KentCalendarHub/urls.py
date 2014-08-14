from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'KentCalendarHub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^studentsite/', include('StudentSite.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/kentdenver.png')),

)