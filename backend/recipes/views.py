from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RecipeSerializer
from django.shortcuts import get_list_or_404,get_object_or_404
from django.template.defaultfilters import slugify
from rest_framework.views import APIView 
from rest_framework import status
from .models import Recipe


class RecipeListView(APIView):
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
    def get(self, request, *args, **kwargs):
        recipe = get_object_or_404(Recipe,pk=self.kwargs['pk'])
        serializers = RecipeSerializer(recipe)
        return Response(serializers.data)
    

        