from django.urls import path
from landingPage.views import show_landingPage, show_afterLoginlandingPage, register, login_user, logout_user, add_feedback, delete_feedback, show_allFeedback_json, show_userFeedback_json

from core.views import frontpage # dari aplikasi core

app_name = 'landingPage'

urlpatterns = [
    path('', show_landingPage, name='show_landingPage'),
    path('landingpage/', show_afterLoginlandingPage, name='show_afterLoginlandingPage'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('add-feedback/', add_feedback, name='add_feedback'),
    path('delete-task/<int:pk>', delete_feedback, name='delete_feedback'),
    path('json-all/', show_allFeedback_json, name='show_allFeedback_json'),
    path('json-user/', show_userFeedback_json, name='show_userFeedback_json'),
    path('blog/', frontpage, name='frontpage'), # dari aplikasi core
]