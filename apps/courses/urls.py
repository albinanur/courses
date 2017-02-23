from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name = 'index'),
    url(r'^courses$',views.create),
    url(r'^delete/(\d+)$', views.delete),
    url(r'^destroy$', views.destroy)

]
