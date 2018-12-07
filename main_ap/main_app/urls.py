from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.HomeView.as_view(), name='home'),
    #path('header', views.header, name='header'),
    url('^unit$', views.services, name='services'),
    url('^index$', views.index, name='index'),
    url('^contact$', views.contact, name='contact'),
    url('^test$', views.Home.as_view(), name='test'),


]