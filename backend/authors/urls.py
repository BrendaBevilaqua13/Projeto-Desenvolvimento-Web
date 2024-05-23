from django.urls import path
from . import views

urlpatterns = [
        path('api/v1/',views.AuthorView.as_view(),name='authors_api_v1'),
        path('create/api/v1/',views.AuthorCreateView.as_view(),name='author_create_api_v1'),
        path('detail/api/v1/<int:pk>',views.AuthorDetailView.as_view(),name='detail_api_v1'),
  
]