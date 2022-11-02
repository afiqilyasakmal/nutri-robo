from django.urls import path
from user_profile import views
from user_profile.views import logout_user, create_profile, show_profile #show_target_json, create_target_ajax

app_name = 'user_profile'

urlpatterns = [
    path('', create_profile, name='create_profile'),
    path('data_diri/', show_profile, name='show_profile'),
    path('target/', views.PhysicalInfoView.as_view(), name='show_target'),
    path('target/create', views.CreateTarget.as_view(), name='create_target'),
    # path('target/', show_target, name='show_target'),
    # path('target/delete/', views.DeleteTarget.as_view(), name='delete_target'),
    #path('show/', logout_user, name='data_diri')
    path('logout/', logout_user, name='logout_user'),
    # path('crud/',  views.CrudView.as_view(), name='crud_ajax'),
    # path('json/', show_target_json, name="show_target_json"),
    # path('create/', create_target_ajax, name="create_target_ajax"),
]