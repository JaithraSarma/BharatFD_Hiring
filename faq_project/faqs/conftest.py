# conftest.py
import pytest
import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'faq_project.settings'

# Initialize Django
django.setup()

@pytest.fixture(scope='session', autouse=True)
def setup_django_settings():
    """Ensure Django settings are configured for pytest."""
    pass
