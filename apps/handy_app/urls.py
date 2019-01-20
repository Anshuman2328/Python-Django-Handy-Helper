from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.main, name='homepage'),
    url(r'^/add$', views.add),
     url(r'^/processadd$', views.processadd),
   url(r'^/show$', views.show),
    url(r'^/edit$', views.edit),
]