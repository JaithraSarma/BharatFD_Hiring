from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator


def translate_text(text, lang):
    translator = Translator()
    return translator.translate(text, dest=lang).text

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(null=True, blank=True)
    question_bn = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set on update

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = translate_text(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = translate_text(self.question, 'bn')
        super().save(*args, **kwargs)
