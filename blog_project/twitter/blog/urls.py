from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path("", views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/', views.CreatePostView.as_view(), name='post_new'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='post_edit'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approved/', views.comments_approve, name='comment_approve'),
    path('comments/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
]