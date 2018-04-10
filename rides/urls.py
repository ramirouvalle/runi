from django.conf.urls import url
from . import views

app_name = 'rides'
urlpatterns = [
    url(r'^$', views.RidesListView.as_view(), name="rides"),
    url(r'^(?P<pk>[0-9]+)/$', views.RideDetailView.as_view(), name="ride_detail"),
    url(r'^add/$', views.NewRideView.as_view(), name="new_ride"),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.EditRideView.as_view(), name="edit_ride"),
    url(r'^(?P<pk>[0-9]+)/request/$', views.RideRequestView.as_view(), name="ride_request")
]
