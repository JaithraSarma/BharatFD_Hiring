from django.urls import path
from .views import FAQListView  # ✅ Correct import

urlpatterns = [
    path('', FAQListView.as_view(), name='faq-list'),
]
