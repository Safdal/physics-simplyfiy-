from django.contrib import admin
from django.urls import path
from blog import views  # Replace 'blog' with your app's name

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page
    path('', views.post_list, name='post_list'),  # Default route for your app
]

