
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from core.views import (
    frontpage,
    signup,
)
from feed.views import (
    feed,
)
from feed.api import api_add_oink


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),

    path('feed/', feed, name='feed'),

    path('api/add_oink/', api_add_oink, name='api_add_oink'),
]
