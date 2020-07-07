from django.conf.urls import url
from student import views

urlpatterns = [
    url(regex=r'^$', view=views.StudentView.as_view(), name='student_list'),
    url(regex=r'^/(?P<pk>[0-9]+)$', view=views.StudentDetailView.as_view(), name='student_detail')
]