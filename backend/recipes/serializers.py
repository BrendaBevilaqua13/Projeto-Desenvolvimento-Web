from rest_framework import serializers
from .models import Recipe
from collections import defaultdict 

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=('id','title','description','author','is_published','category','preparation_time',\
                'preparation_time_unit','servings','servings_unit','preparation_steps')

    category = serializers.StringRelatedField()

    def validate_title(self, value):
        title = value
        if len(title)<5:
            raise serializers.ValidationError('O titulo deve ter mais que 5 caracter')

        return title
    
    def validate(self, attrs):
        super_validate = super().validate(attrs)
        cd = attrs
        _my_errors = defaultdict(list)
        title = cd.get('title')
        description = cd.get('description')
        if title == description:
            _my_errors['title'].append('Cannot be equal to description'),
            _my_errors['description'].append('Cannot be equal to title')
        
        if _my_errors:
            raise serializers.ValidationError(_my_errors)
        
        return super_validate