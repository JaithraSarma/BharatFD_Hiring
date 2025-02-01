from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['question', 'answer', 'question_hi', 'question_bn', 'answer_hi', 'answer_bn']

    def get_translated_question(self, obj):
        language_code = self.context.get('language_code', 'en')  # Pass 'language_code' in context
        return obj.get_translated_question(language_code)

    def get_translated_answer(self, obj):
        language_code = self.context.get('language_code', 'en')  # Pass 'language_code' in context
        return obj.get_translated_answer(language_code)
