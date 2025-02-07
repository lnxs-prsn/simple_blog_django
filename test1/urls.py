from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView, CategoryListView, LikeView, AddCategoryView, AddCommentView


urlpatterns = [
    # path('', views.home, name='home'),
    # path('home2', views.home2, name='home2'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove/', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>/', LikeView, name='like_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    
]
