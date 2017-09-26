from django.conf.urls import url
from . import views

app_name = 'rides'
urlpatterns = [
    url(r'^$', views.RidesListView.as_view(), name="rides"),
    url(r'^(?P<pk>[0-9]+)', views.RideDetailView.as_view(), name="ride_detail")
]