from django.urls import path
from . import views
from .views import SearchResultsView

app_name = "posts"

urlpatterns = [
    path('post', views.post_list, name='post_list'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/rating/', views.add_rating_to_post, name='add_rating_to_post'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]