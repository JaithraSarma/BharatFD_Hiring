from googletrans import Translator
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

def google_translate(text, target_lang):
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)
    return translated.text

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = models.TextField(blank=True, null=True)
    answer_bn = models.TextField(blank=True, null=True)

    def translate_fields(self):
        if not self.question_hi:
            self.question_hi = self.translate_to_hindi(self.question)
        if not self.question_bn:
            self.question_bn = self.translate_to_bengali(self.question)

        if not self.answer_hi:
            self.answer_hi = self.translate_to_hindi(self.answer)
        if not self.answer_bn:
            self.answer_bn = self.translate_to_bengali(self.answer)

    def translate_to_hindi(self, text):
        return google_translate(text, "hi")

    def translate_to_bengali(self, text):
        return google_translate(text, "bn")

    def get_translated_question(self, language_code):
        """Get the translated question based on the given language code."""
        if language_code == 'hi':
            return self.question_hi or self.question  # Fallback to original question if translation is missing
        elif language_code == 'bn':
            return self.question_bn or self.question  # Fallback to original question if translation is missing
        return self.question  # Default to original question if language is not supported

    def get_translated_answer(self, language_code):
        """Get the translated answer based on the given language code."""
        if language_code == 'hi':
            return self.answer_hi or self.answer  # Fallback to original answer if translation is missing
        elif language_code == 'bn':
            return self.answer_bn or self.answer  # Fallback to original answer if translation is missing
        return self.answer  # Default to original answer if language is not supported

    def __str__(self):
        return self.question
