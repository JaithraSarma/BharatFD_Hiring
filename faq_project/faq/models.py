from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG Editor support

    # Translations
    question_hi = models.TextField(blank=True, null=True)  # Hindi
    question_bn = models.TextField(blank=True, null=True)  # Bengali

    def get_translated_question(self, lang='en'):
        cache_key = f'faq_{self.id}_lang_{lang}'
        cached_translation = cache.get(cache_key)

        if cached_translation:
            return cached_translation

        translation = getattr(self, f'question_{lang}', self.question)
        cache.set(cache_key, translation, timeout=86400)
        return translation

    def __str__(self):
        return self.question
