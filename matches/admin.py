from django.contrib import admin
from .models import InterpretationRequest, Trait

class InterpretaionRequestAdmin(admin.ModelAdmin):
    pass
    
class TraitAdmin(admin.ModelAdmin):
    pass


admin.site.register(InterpretationRequest, InterpretaionRequestAdmin)
admin.site.register(Trait, TraitAdmin)