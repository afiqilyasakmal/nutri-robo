from django.urls import path
from . import views

app_name = 'target_profile'

urlpatterns = [
    path('accounts/profile/', views.UserProfile.as_view(), name='profile'),
    path('create-profile/', views.CreateProfile.as_view(), name='create_profile'),
    path('profile-create-or-update/', views.CreateOrUpdateProfile.as_view(), name='profile_coru'),
    path('target-update/', views.CreateOrUpdatePhysicalInfo.as_view(), name='target_coru'),
    path('accounts/profile/json', views.CreateOrUpdatePhysicalInfo.as_view(), name='show_json'),
]