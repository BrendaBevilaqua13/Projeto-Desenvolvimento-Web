from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RecipeSerializer
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView 
from .models import Recipe


class RecipeListView(APIView):
    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        serializers = RecipeSerializer(recipes,many=True)
        return Response(serializers.data)
