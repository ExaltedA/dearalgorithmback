from django.urls import path
from core.views import *


urlpatterns = [

    path('posts/', PostList.as_view()),


]
