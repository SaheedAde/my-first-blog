from django.conf.urls import url
from . import views  # from current directory import views

urlpatterns = [
    # adebiodun.com
    url(r'^$', views.post_list, name='post_list'),

    # adebiodun.com/post/129/
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail')
]
