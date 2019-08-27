
from django.conf.urls import url
from django.contrib import admin
from contact.views import index, detail, add_people, record

urlpatterns = [
    url(r'^index/$', index, name="index"),
    url(r'^detail/(\d+)$', detail),
    url(r'^add_people$', add_people),
    url(r'^record$', record, name="record"),
]
