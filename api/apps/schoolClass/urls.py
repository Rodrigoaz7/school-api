from django.conf.urls import url
from schoolClass import views

urlpatterns = [
    url(regex=r'^$', view=views.ClassView.as_view(), name='class_list'),
    url(regex=r'^/(?P<pk>[0-9]+)$', view=views.ClassDetailView.as_view(), name='class_detail')
]