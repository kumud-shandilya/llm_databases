from rest_framework import serializers
from llm.models import UserPrompt

class UserPromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPrompt
        fields = ['user_query', 'table_name']