from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FAQ
from .serializers import FAQSerializer
from django.core.cache import cache

class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')
        cached_data = cache.get(f'faqs_{lang}')
        
        if cached_data:
            return Response(cached_data)

        faqs = FAQ.objects.all()
        data = [{"id": f.id, "question": f.get_translation(lang), "answer": f.answer} for f in faqs]
        cache.set(f'faqs_{lang}', data, timeout=60 * 5)  # Cache for 5 minutes

        return Response(data)
