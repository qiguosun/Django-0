from django.urls import path
from . import views  # . indicate current directory
# we refer to this as a url configuration, map 1 or more path objects to view functions

app_name = 'movies'
urlpatterns = [
    # root of this app # not pass a function, simply passing a reference to it
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]
