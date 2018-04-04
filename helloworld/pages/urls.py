from django.conf.urls import url
from .import views

urlpatterns = [
    # url(r'^$',views.home_new, name='home_new'),
    url(r'^home/$',views.Home_New.as_view(),name='home_new'),
    url(r'^index/$',views.AboutPageView.as_view(),name='AboutPageView'),
]