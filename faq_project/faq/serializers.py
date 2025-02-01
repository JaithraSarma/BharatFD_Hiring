from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    question_translated = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'question_translated']

    def get_question_translated(self, obj):
        request = self.context.get('request')
        lang = request.GET.get('lang', 'en')
        return obj.get_translated_question(lang)
