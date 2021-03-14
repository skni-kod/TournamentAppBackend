from django.contrib import admin
from django.conf.urls import url
from Api.views import *



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/player/$', PlayerViewSetList.as_view(), name='Player_List'),
    url(r'^api/player/(?P<pk>\d+)/$', PlayerViewSetDetail.as_view(), name='Player_Detail')
]
