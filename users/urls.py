from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^register/$', views.register, name="register"),
    url(r'^(?P<username>\w+)/rides/$', views.UserRidesView.as_view(), name="user_ride_list"),
    url(r'^(?P<username>\w+)/$', views.UserProfile.as_view(), name="user_profile"),
]
