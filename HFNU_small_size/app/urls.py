from django.urls import path, include

import app.views


urlpatterns = [
    path('hello_world', app.views.hello_world),
    path('article',app.views.article_content),
    path('index',app.views.get_index_page),
    path('detail/<int:article_id>',app.views.get_detail_page)
]