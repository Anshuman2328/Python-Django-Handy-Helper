from django.conf.urls import url, include


urlpatterns = [
    url(r'^',include ('apps.app_one.urls')),
    url(r'^handy_app', include('apps.handy_app.urls'))
]
