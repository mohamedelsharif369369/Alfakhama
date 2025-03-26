from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('profile',views.profile,name='profile'),
    path('profile/edit',views.profile_edit,name='profileEdit'),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('loggedOut/', auth_views.LoginView.as_view(template_name='registration/logged_out.html'), name='loggedOut'),
    path('password_change_form/', auth_views.LoginView.as_view(template_name='registration/password_change_form.html'), name='password_change_form'),
    path('password_reset_complete/', auth_views.LoginView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('password_reset_confirm/', auth_views.LoginView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_done/', auth_views.LoginView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_email/', auth_views.LoginView.as_view(template_name='registration/password_reset_email.html'), name='password_reset_email'),
    path('password_reset_form/', auth_views.LoginView.as_view(template_name='registration/password_reset_form.html'), name='password_reset_form'),
]
