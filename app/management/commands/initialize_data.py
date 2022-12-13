from django.core.management.base import BaseCommand

from bankaccounts.factories import BankAccountFactory


class Command(BaseCommand):
    def handle(self, *args, **options):
        account_one = BankAccountFactory(balance=10000)
        account_two = BankAccountFactory(balance=2000)

        account_one.transfer(amount=250, target=account_two)
        account_one.transfer(amount=100, target=account_two)
        account_two.transfer(amount=700, target=account_one)
