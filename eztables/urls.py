# -*- coding: utf-8 -*-
from django.conf.urls import include, url
# project imports
from eztables.demo import views


# enable django admin
from django.contrib import admin ; admin.autodiscover()


urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^client-side$', views.ClientSideView.as_view(), name='client-side'),
	url(r'^server-side$', views.ServerSideView.as_view(), name='server-side'),
	url(r'^server-side-search$', views.ServerSideSearchView.as_view(), name='server-side-search'),
	url(r'^server-side-objects$', views.ServerSideObjectsView.as_view(), name='server-side-objects'),
	url(r'^server-side-custom$', views.ServerSideCustomView.as_view(), name='server-side-custom'),
	url(r'^defered-loading$', views.DeferredLoadingView.as_view(), name='deferred-loading'),
	url(r'^localization$', views.LocalizationView.as_view(), name='localization'),
	url(r'^browsers/', include([
		url(r'^default$', views.FormattedBrowserDatatablesView.as_view(), name='DT-browsers-default'),
		url(r'^objects$', views.ObjectBrowserDatatablesView.as_view(), name='DT-browsers-objects'),
		url(r'^custom$', views.CustomBrowserDatatablesView.as_view(), name='DT-browsers-custom'),
	])),
	
	url(r'^js/', include('djangojs.urls')),

	url(r'^admin/', include(admin.site.urls)), # django-contrib-adminn
]
