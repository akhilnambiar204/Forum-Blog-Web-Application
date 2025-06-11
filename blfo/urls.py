from django.urls import path
from . import views
from django.shortcuts import redirect


urlpatterns = [
    path('', lambda req: redirect('/blfo/')),
    path('blfo/', views.blfo, name='blfo'),
    path('forump/', views.forump, name='forump'),
    path('post/', views.post, name='post'),
    path('create/', views.create, name='create'),
    path('details/', views.details, name='details'),
    path('create_forum/', views.create_forum, name='create_forum'),
    path('create_comment/', views.create_comment, name='create_comment'),
    path('blog_panel/', views.blog_panel, name='create_comment'),
    path('blog_view/', views.blog_view, name='create_comment'),
    path('create_blog/', views.create_blog, name='create_comment'),
]