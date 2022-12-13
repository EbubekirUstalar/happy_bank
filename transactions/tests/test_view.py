from django.test import TestCase, Client

from bankaccounts.factories import BankAccountFactory


class TransactionViewTestCase(TestCase):
    '''
        python manage.py test transactions.tests.test_view.TransactionViewTestCase
    '''

    def setUp(self):
        client = Client()

        account_one = BankAccountFactory(balance=10000)
        account_two = BankAccountFactory(balance=2000)

        account_one.transfer(amount=250, target=account_two)
        account_one.transfer(amount=100, target=account_two)
        account_two.transfer(amount=700, target=account_one)
        account_two.transfer(amount=300, target=account_one)
        account_two.transfer(amount=200, target=account_one)

    def test_transaction_list_view(self):
        response = self.client.get('/onlinebanking/transactions/')
        self.assertEqual(response.status_code, 200)

    def test_transaction_list_view_query_count(self):
        # There are too many queries fired on this page, why that is? Please fix it without changing the tests
        with self.assertNumQueries(2):
            response = self.client.get('/onlinebanking/transactions/')
            self.assertEqual(response.status_code, 200)
