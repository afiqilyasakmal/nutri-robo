from django.urls import path
from authentication.views import login, register, logout_user, show_userFeedback, add_feedback

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout_user'),
    path('userfeedback/', show_userFeedback, name='show_userFeedback'),
    path('addfeedback/', add_feedback, name='add_feedback'),
]