from django.conf.urls import url
from . import views

app_name = 'app'

urlpatterns = [
    url(r'^$', views.CompanyList.as_view(), name='company_list'),
    url(r'^register/$', views.CompanyCreate.as_view(), name='company_create'),
    url(r'^register/success/(?P<pk>[0-9]+)/$', views.CompanyCreateAfter.as_view(), name='company_create_after'),
    url(r'^book/(?P<pk>[0-9]+)/$', views.CompanyBook.as_view(), name='company_book'),
]
