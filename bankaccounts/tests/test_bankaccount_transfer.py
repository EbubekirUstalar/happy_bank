from django.test import TestCase
from bankaccounts.models import BankAccount, BankAccountOwner

from transactions.exceptions import TransactionException


class BankAccountTransferTestCase(TestCase):

    def setUp(self):
        self.owner_one = BankAccountOwner.objects.create(given_name="John", family_name="Doe", email="johndoe@gmail.com")
        self.owner_two = BankAccountOwner.objects.create(given_name="Jane", family_name="Doe", email="janedoe@gmail.com")

        self.account_one = BankAccount.objects.create(owner=self.owner_one, balance=1000, iban="dummy_iban_1")
        self.account_two = BankAccount.objects.create(owner=self.owner_two, balance=250, iban="dummy_iban_2")

    def test_successful_transaction_values(self):
        transaction_in, transaction_out = self.account_one.transfer(amount=100, target=self.account_two)
        self.assertEqual(transaction_in.value, transaction_out.value * -1)

    def test_negative_transaction_value(self):
        with self.assertRaisesMessage(TransactionException, "A transfer value must be a positive decimal"):
            self.account_one.transfer(amount=-250, target=self.account_two)


