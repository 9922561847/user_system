from django.urls import path
from user_system_app import views

urlpatterns = [
    path('user/',views.userregistration,name='userregistration'),
    path('signup/',views.sign_up,name='sign_up'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.user_profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('userdetail/<int:id>',views.user_detail,name='userdetail'),



]