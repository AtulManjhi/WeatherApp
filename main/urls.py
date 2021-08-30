from django.urls import path
from main import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.index, name = 'index')
]
urlpatterns += staticfiles_urlpatterns()