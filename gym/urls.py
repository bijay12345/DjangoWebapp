from django.urls import path,include
from . import views
from .views import PostListView, VideoListView,VideoDetailView,PostDetailView,PostCreateView
from .views import PostUpdateView,PostDeleteView
from .views import VideoCreateView,VideoUpdateView,VideoDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('video/', VideoListView.as_view(), name='video'),
    path('videod/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('video/<int:pk>/update/', VideoUpdateView.as_view(), name='video-update'),    
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('video/<int:pk>/delete/', VideoDeleteView.as_view(), name='video-delete'),
    path('video/new/', VideoCreateView.as_view(), name='video-create'),
    path('about/',views.about,name='about')
]
