from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RecipeSerializer
from django.shortcuts import get_list_or_404,get_object_or_404
from django.template.defaultfilters import slugify
from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Recipe


class RecipeListView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        serializers = RecipeSerializer(recipes,many=True)
        return Response(serializers.data)
    
    def post(self, request, *args, **kwargs):
        serializer = RecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer)
        serializer.save(
            author_id=1,category_id=1
        )
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class RecipeDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        recipe = get_object_or_404(Recipe,pk=self.kwargs['pk'])
        serializers = RecipeSerializer(recipe)
        return Response(serializers.data)
    
    def patch(self, request, *args, **kwargs):
        recipe = get_object_or_404(Recipe,pk=self.kwargs['pk'])
        serializer = RecipeSerializer(instance=recipe,
                                       data=request.data,
                                       partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            author_id=1,category_id=1
        )
        return Response(serializer.data)
    
    def delete(self, request, *args, **kwargs):
        recipe = get_object_or_404(Recipe,pk=self.kwargs['pk'])
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        