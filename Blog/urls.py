from django.conf.urls import url
from . import views  # from current directory import views

urlpatterns = [
    # adebiodun.com
    url(r'^$', views.post_list, name='post_list'),
]
