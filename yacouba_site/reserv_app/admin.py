from django.contrib import admin
from .models import Evenement

class EvenementAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        # Vérifiez si l'utilisateur est un superutilisateur ou s'il a la permission 'can_view_all_events'
        if request.user.is_superuser or request.user.has_perm('events.can_view_all_events'):
            return True
        return False

admin.site.register(Evenement)

# Register your models here.
