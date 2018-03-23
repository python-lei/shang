from django.conf.urls import url

from app01 import views

urlpatterns=[
    url(r"^index$",views.index),
    url(r"^post$",views.post),
    url(r"^get_post",views.get_post),

]