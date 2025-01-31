from django.test import TestCase
from django.utils import timezone
from faqs.models import FAQ
import os
import django
import unittest
import pytest

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'faq_project.settings'

# Initialize Django
django.setup()

class FAQTestCase(unittest.TestCase):

    def test_create_faq(self):
        # Manually set created_at
        faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework.",
            question_hi="Django क्या है?",
            question_bn="ডjango কী?",
            created_at=timezone.now()  # Manually setting created_at
        )
        
        self.assertEqual(faq.question, "What is Django?")
        self.assertEqual(faq.answer, "Django is a web framework.")
        self.assertEqual(faq.question_hi, "Django क्या है?")
        self.assertEqual(faq.question_bn, "ডjango কী?")

