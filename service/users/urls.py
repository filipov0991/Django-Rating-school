from django.urls import path
from .views import UserView, UsersView, RegistrUserView, LoginUserView, login_view, logout_view, profile_edit, profile
# from .views import PaginatorView, StatsView

app_name = "users"
# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('api/users', UsersView.as_view()),
    path('api/users/<str:username>', UserView.as_view()),
    path('edit/<str:username>', UserView.as_view()),
    path('registration/', RegistrUserView.as_view(), name='registration'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('login2/', login_view, name='login2'),
    path('logout', logout_view, name='logout'),
    path('profile', profile, name='profile'),
    path('profile/edit/', profile_edit, name='profile_edit'),
]