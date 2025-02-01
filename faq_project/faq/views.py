from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    def get(self, request):
        language_code = request.GET.get('lang', 'en')  # Example: 'lang' parameter from the URL (default 'en')
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True, context={'language_code': language_code})
        return Response(serializer.data)
