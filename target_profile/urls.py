from django.urls import path
from . import views
from target_profile.views import CreateOrUpdatePhysicalInfo, UserProfile
from  target_profile.flutter_views import show_user_profile, show_user_target, update_profile, update_target #profile_flutter, coru_profile_flutter, target_flutter, coru_target_flutter

app_name = 'target_profile'

urlpatterns = [
    path('accounts/profile/', views.UserProfile.as_view(), name='profile'),
    path('create-profile/', views.CreateProfile.as_view(), name='create_profile'),
    path('profile-create-or-update/', views.CreateOrUpdateProfile.as_view(), name='profile_coru'),
    path('target-update/', views.CreateOrUpdatePhysicalInfo.as_view(), name='target_coru'),
    path('accounts/profile/json/', CreateOrUpdatePhysicalInfo.show_json, name='show_json'),
    #path('accounts/detail/profile/json/', UserProfile.show_profile_in_json, name='show_profile_in_json'),
    #path('accounts/detail/target/json/', UserProfile.show_target_in_json, name='show_target_in_json'),

    # path('flutter/profile/<str:username>', profile_flutter, name="flutter-profile"),
    # path('flutter/target/<str:username>', target_flutter, name="flutter-target"),
    # path('flutter/coru-profile', coru_profile_flutter, name="flutter-coru-profile"),
    # path('flutter/coru-target', coru_target_flutter, name="flutter-coru-target"),
    path('flutter/profile/<str:username>', show_user_profile, name="show_user_profile"),
    path('flutter/target/<str:username>', show_user_target, name="show_user_target"),
    path('flutter/update/profile/', update_profile, name="update_profile"),
    path('flutter/update/target/', update_target, name="update_target")
]