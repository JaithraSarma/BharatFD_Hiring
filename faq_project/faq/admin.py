from django.contrib import admin
from .models import FAQ

# Avoid duplicate registration
try:
    admin.site.unregister(FAQ)
except admin.sites.NotRegistered:
    pass

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'question_hi', 'question_bn')
    fields = ('question', 'answer', 'question_hi', 'question_bn')

    def save_model(self, request, obj, form, change):
        obj.translate_fields()  # Translate fields before saving
        super().save_model(request, obj, form, change)

admin.site.register(FAQ, FAQAdmin)
