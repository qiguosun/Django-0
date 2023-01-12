from django.urls import path
from . import views  # . indicate current directory
# we refer to this as a url configuration, map 1 or more path objects to view functions
urlpatterns = [
    # root of this app # not pass a function, simply passing a reference to it
    path('', views.index, name='index')
]
