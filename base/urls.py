from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',  views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/',  views.registerPage, name="register"),
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    path('update-user/', views.updateUser, name='update-user'),
    path('topics/', views.topicsPage, name='topics'),
    path('activities/', views.activitiesPage, name='activities'),

    path('reset/', auth_views.PasswordResetView.as_view(template_name='base/password_reset.html',
                                                        email_template_name='base/password_reset_email.html',
                                                        subject_template_name='base/password_reset_subject.txt'),
         name='password_reset'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='base/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done',
        auth_views.PasswordResetDoneView.as_view(template_name='base/password_reset_done.html'),
        name='password_reset_done'),

    path('reset/complete',
        auth_views.PasswordResetCompleteView.as_view(template_name='base/password_reset_complete.html'),
        name='password_reset_complete'),
]
