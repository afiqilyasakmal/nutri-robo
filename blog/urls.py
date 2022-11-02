from django.urls import path

from . import views

urlpatterns = [
    path('blog/<slug:slug>/', views.detail, name="post_detail"),
]

