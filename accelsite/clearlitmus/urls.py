from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='clearlitmusindex'),
    url(r'^last.html$', views.simple_html, name='clearlitmussimple'),
]