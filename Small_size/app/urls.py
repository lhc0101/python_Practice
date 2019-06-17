from django.urls import path, include

import app.views


urlpatterns = [
    path('hello_world', app.views.hello_world)
]