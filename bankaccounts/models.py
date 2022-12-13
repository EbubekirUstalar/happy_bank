from django.conf import settings
from django.db import models
from django.db.transaction import atomic
from django.utils.translation import gettext_lazy as _

from transactions.exceptions import TransactionException


class BankAccount(models.Model):
    owner = models.ForeignKey(
        "bankaccounts.BankAccountOwner",
        verbose_name=_("Account owner"),
        on_delete=models.CASCADE,
    )
    iban = models.CharField(max_length=34, unique=True, verbose_name=_("IBAN"))
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Balance")
    )

    @atomic
    def transfer(self, amount, target):
        # transfer amounts must be positive
        if amount <= 0:
            raise TransactionException(_("A transfer value must be a positive decimal"))

        if self.iban == target.iban:
            raise TransactionException(_("A transfer should not happen on the same account"))

        # add transactions
        from transactions.models import Transaction

        if amount > self.balance:
            raise TransactionException(_("A transfer value must be smaller than your current balance"))

        if amount > settings.MAX_TRANSACTION_AMOUNT:
            raise TransactionException(_("A transfer value must be smaller than max transaction amount"))

        transaction_out = Transaction.objects.create(
            account=self, remote=target, value=amount * -1
        )
        transaction_in = Transaction.objects.create(
            account=target, remote=self, value=amount
        )
        return transaction_out, transaction_in


class BankAccountOwner(models.Model):
    given_name = models.CharField(max_length=50, verbose_name=_("Given name"))
    family_name = models.CharField(max_length=50, verbose_name=_("Family name"))
    email = models.EmailField(verbose_name=_("Email"))

    def notify_about_transaction(self, transaction):
        pass
