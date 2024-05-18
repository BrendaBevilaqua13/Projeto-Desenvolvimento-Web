from django.urls import path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('recipes/api/v1/',views.RecipeListView.as_view(),name='recipes_api_v1')
]
