from django.contrib import admin
from django.urls import path
from blog import views  # Import your app views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='post_list'),  # Add your app's view
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
