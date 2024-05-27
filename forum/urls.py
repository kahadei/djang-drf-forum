from django.urls import path
from rest_framework import routers
from forum import views

router = routers.DefaultRouter()


urlpatterns = [
    # FORUMS
    path('api/new-forum/', views.create_forum_view, name="new-forum"),
    path('api/forums/', views.forums_list_view, name="forums"),
    path('api/forum/<int:pk>/', views.forum_details_view, name="forum-details"),
    path('api/join-forum/<int:pk>/', views.join_forum_view, name="join-forum"),

    # MESSAGES
    path('api/new-message/', views.create_message_view, name="new-message"),

    # PROFILE
    path('api/new-profile-data/', views.create_profile_view, name="new-profile"),
    path('api/users-list/', views.users_list_view, name="users-list"),
    path('api/user-profile/<int:pk>/', views.profile_details_view, name="profile-details"),
    path('api/user-register', views.create_user_view, name="register-user"),

]

urlpatterns += router.urls