from django.contrib import admin

from transactions import models


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass
