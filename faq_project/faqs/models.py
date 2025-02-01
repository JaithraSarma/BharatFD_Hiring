from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

def translate_text(text, dest_language):
    translator = Translator()
    return translator.translate(text, dest=dest_language).text

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = translate_text(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = translate_text(self.question, 'bn')
        super().save(*args, **kwargs)

