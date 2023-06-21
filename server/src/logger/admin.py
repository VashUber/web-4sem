from django.contrib import admin

from .models import VisitModel


# Register your models here.
class VisitAdmin(admin.ModelAdmin):
    list_display = ('user','url','start_at','execution_time',"http_user_agent")


admin.site.register(VisitModel, VisitAdmin)
