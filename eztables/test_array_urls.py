# -*- coding: utf-8 -*-

# stdlib imports
from django.conf.urls import url
# project imports
from eztables.demo import views


urlpatterns = [
	url(r'^$', views.BrowserDatatablesView.as_view(), name='browsers'),
	url(r'^formatted/$', views.FormattedBrowserDatatablesView.as_view(), name='formatted-browsers'),
	url(r'^custom/$', views.CustomBrowserDatatablesView.as_view(), name='custom-browsers'),
	url(r'^special/$', views.SpecialCaseDatatablesView.as_view(), name='special'),
]
