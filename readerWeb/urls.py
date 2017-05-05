from django.conf.urls import url
from readerWeb.views import ReadCommendList, ReadCommendItem

urlpatterns = [
    url(r'^list/', ReadCommendList.as_view()),
    url(r'^item/', ReadCommendItem.as_view()),
]
