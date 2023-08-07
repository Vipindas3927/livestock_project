
from django.conf import settings
#from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# Add the following line at the end of your urlpatterns



urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup, name="signup"),
    path('home', views.home, name="home"),
    path('logout/', views.logout_view, name="logout"),   
    path('add/', views.add, name="add"),  
    path('delete/<int:id>/', views.delete_view, name="delete"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('upload_display_video/', views.upload_display_video, name="upload_display_video"),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload_video, name='upload_video'),
    # path('list/', views.video_list, name='video_list'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)