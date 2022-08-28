from django.urls import path
from . import views


urlpatterns = [
    path('', views.BlogPostView.as_view(), name='blogposts'),
    path('post/<str:slug>/', views.BlogPostCategoryView.as_view(), name='category'),
    path('post/<str:category>/<str:slug>.html', views.BlogDetailsView.as_view(), name='details'),

] 
