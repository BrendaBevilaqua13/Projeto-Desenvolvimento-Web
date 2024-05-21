from django.urls import path
from recipes import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = 'recipes'

urlpatterns = [
    path('recipes/api/v1/',views.RecipeListView.as_view(),name='recipes_api_v1'),
    path('recipes/api/v1/<int:pk>/',views.RecipeDetailView.as_view(),name='recipes_api_v1_detail'),
    path('recipes/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('recipes/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('recipes/api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
