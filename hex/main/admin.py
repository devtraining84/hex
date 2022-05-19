from django.contrib import admin
from .models import MembershipModels


# Register your models here.
@admin.register(MembershipModels)
class MembershipModels(admin.ModelAdmin):
    pass



