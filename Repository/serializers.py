from rest_framework import serializers
from Repository.models import Questions

class QuestionSereializer(serializers.Serializer):
    title=serializers.CharField(max_length=100)
    language=serializers.ChoiceField(choices=Questions.language_choice,default='python')
    difficulty_level=serializers.ChoiceField(choices=Questions.DIFFICULTY_LEVEL,default='easy')
    notes=serializers.CharField()
    topic=serializers.CharField()
    published_date=serializers.DateTimeField(read_only=True)
    sample_input=serializers.CharField()
    sample_output=serializers.CharField()
    is_active=serializers.BooleanField()