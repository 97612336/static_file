from django.contrib import admin
from django.urls import path

from read_and_write.views import index, upload_file

app_name = 'read_and_write'
urlpatterns = [
    path('', index,name="index"),
    path('upload_file/', upload_file, name="upload_file"),
]
