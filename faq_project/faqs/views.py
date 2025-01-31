from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import FAQ
from django.core.cache import cache

class FAQListView(View):
    def get(self, request, *args, **kwargs):
        lang = request.GET.get('lang', 'en')  # Default to English
        cache_key = f"faq_list_{lang}"  # Unique cache key for each language
        data = cache.get(cache_key)  # Try fetching from cache

        if not data:  # If not in cache, fetch from DB
            data = list(FAQ.objects.all().values('id', 'question', 'answer'))
            cache.set(cache_key, data, timeout=3600)  # Cache for 1 hour

        return JsonResponse(data, safe=False)
