import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from faq.models import FAQ

@pytest.mark.django_db  # Use database during test
def test_faq_list_api():
    client = APIClient()
    url = reverse('faq-list')  # Ensure this matches the URL name in faq/urls.py
    response = client.get(url)

    assert response.status_code == 200  # Ensure API is working
    assert response.json() == []  # Expect an empty list initially
