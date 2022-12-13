from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from transactions.exceptions import (
    TransactionInsufficientFundsException,
    TransactionImmutableException,
)


class Transaction(models.Model):
    account = models.ForeignKey(
        "bankaccounts.BankAccount",
        verbose_name=_("Account"),
        null=True,
        on_delete=models.PROTECT,
        related_name="account",
    )
    remote = models.ForeignKey(
        "bankaccounts.BankAccount",
        verbose_name=_("Remote account"),
        on_delete=models.PROTECT,
        related_name="remote",
    )
    value = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Value")
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))

    def save(self, *args, **kwargs):
        if self.pk:
            raise TransactionImmutableException(
                _("An existing transaction cannot be modified")
            )
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.pk:
            raise TransactionImmutableException(
                _("An existing transaction cannot be deleted")
            )
        super().delete(*args, **kwargs)

    def validate_bigger_than_100(value):
        if value % 2 != 0:
            raise ValidationError(
                _('%(value)s is not an even number'),
                params={'value': value},
            )


@receiver(post_save, sender=Transaction)
def transaction_created_update_balance(sender, instance, created, **kwargs):
    # check available funds when transferring out
    if instance.value < 0 and instance.account.balance < instance.value * -1:
        raise TransactionInsufficientFundsException(_("Insufficient funds"))

    # update account balance
    instance.account.balance += instance.value
    instance.account.save(update_fields=["balance"])
