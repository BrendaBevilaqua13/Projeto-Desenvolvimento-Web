from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from .serializers import Authorerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework import status
from django.shortcuts import get_object_or_404 
from .permissions import IsOwner


class AuthorView(APIView):
   permission_classes = [IsAuthenticated,]
   def get(self, request, *args, **kwargs):
      User = get_user_model()
      user = User.objects.filter(username=self.request.user.username)
      serializers = Authorerializer(user,many=True)
      return Response(serializers.data)
   


class AuthorCreateView(APIView):

   def post(self, request, *args, **kwargs):
      serializer = Authorerializer(data=request.data)
      print()
      password = make_password(request.data['password'])
      serializer.is_valid(raise_exception=True)
      serializer.save(pk=request.user.id,password=password)
      return Response(serializer.data,status=status.HTTP_201_CREATED)


class AuthorDetailView(APIView):
   permission_classes = [IsAuthenticated,]

   def get_object(self):
        pk = self.kwargs.get('pk','')
        obj = get_object_or_404(get_user_model(),pk=pk)

        self.check_object_permissions(self.request,obj)

        return obj

   def get_permissions(self):
      if self.request.method in ['PATCH','DELETE']:
         return [IsOwner(), ]

      return super().get_permissions()


   def patch(self, request, *args, **kwargs):
      author = self.get_object()
      serializer = Authorerializer(instance=author,
                                       data=request.data,
                                       partial=True)
      serializer.is_valid(raise_exception=True)
      serializer.save( )
      return Response(serializer.data)
   
   def delete(self, request, *args, **kwargs):
      author = self.get_object()
      author.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
