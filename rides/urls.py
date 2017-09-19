from django.conf.urls import url
from . import views

app_name = 'rides'
urlpatterns = [
    url(r'^$', views.RidesListView.as_view(), name="rides"),
]