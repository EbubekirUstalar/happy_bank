from django.contrib import admin

from bankaccounts import models


@admin.register(models.BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BankAccountOwner)
class BBankAccountOwnerAdmin(admin.ModelAdmin):
    pass
