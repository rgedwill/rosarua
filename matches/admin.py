from django.contrib import admin
from .models import InterpretationRequest, Trait

class InterpretaionRequestAdmin(admin.ModelAdmin):
    list_display = ('datetime_created', 'traits')
    
class TraitAdmin(admin.ModelAdmin):
    list_display = ('name')


admin.site.register(InterpretationRequest, InterpretaionRequestAdmin)
admin.site.register(Trait, TraitAdmin)