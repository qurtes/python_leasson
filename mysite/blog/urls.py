from rest_framework import routers
from .api import views as apiviews
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

router = routers.DefaultRouter()
router.register(r'posts', apiviews.PostViewSet)
router.register(r'postspoints', apiviews.PostPointViewsSet)

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>', views.post_list, name='post_list_by_tag'),
    # path('login', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LoginView.as_view(), name='logout'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('post-add/', views.post_add, name='post_add'),
    path('post-edit/<int:post_id>/', views.post_edit, name='post_edit'),
    path('post-delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('post_point_list/<int:post_id>/', views.post_point_list, name='post_point_list'),
    path('post_point_add/<int:post_id>/', views.post_point_add, name='post_point_add'),
    path('post_point_edit/<int:post_id>/', views.post_point_edit, name='post_point_edit'),
    path('post_point_delete/<int:post_point_id>/', views.post_point_delete, name='post_point_delete'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('profile/', views.edit_profile, name='edit_profile'),
    path('add_to_favourite/<int:post_id>/', views.add_to_favourite, name='add_to_favourite'),
    path('delete_from_favourite/<int:post_id>/', views.delete_from_favourite, name='delete_from_favourite'),
    path('favourite_posts/', views.favourite_posts, name='favourite_posts'),
    path('delete_from_favourite_in_dashboard/<int:post_id>/', views.delete_from_favourite_in_dashboard,
         name='delete_from_favourite_in_dashboard'),
    path('api/', include(router.urls)),
    path('api/post/', apiviews.post_list, name='post'),
    path('api/post/<pk>/', apiviews.post_detail, name='post_detail'),
    path('api/post_create/', apiviews.post_create, name='post_create'),
    path('api/post_point_create/', apiviews.post_point_create, name='post_point_create'),
    path('api/comment_create/', apiviews.comment_create, name='comment_create'),
    path('api/post_update/<pk>/', apiviews.post_update, name='post_update'),
    path('api/post_point_update/<pk>/', apiviews.post_point_update, name='post_point_update'),
    path('api/comment_update/<pk>/', apiviews.comment_update, name='comment_update'),
    path('api/comment_delete/<pk>/', apiviews.comment_delete, name='comment_delete'),
    path('api/post_delete/<pk>/', apiviews.post_delete, name='post_delete'),
    path('api/post_point_delete/<pk>/', apiviews.post_point_delete, name='post_point_delete'),

]