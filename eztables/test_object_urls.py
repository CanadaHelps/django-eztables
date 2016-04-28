# -*- coding: utf-8 -*-

# stdlib imports
from django.conf.urls import patterns, url
# project imports
from eztables.demo import views


urlpatterns = [
	url(r'^$', views.ObjectBrowserDatatablesView.as_view(), name='browsers'),
	url(r'^formatted/$', views.FormattedObjectBrowserDatatablesView.as_view(), name='formatted-browsers'),
	url(r'^custom/$', views.CustomObjectBrowserDatatablesView.as_view(), name='custom-browsers'),
	url(r'^special/$', views.SpecialCaseDatatablesView.as_view(), name='special'),
]
