from django.test import TestCase


class TransactionImmutableTestCase(TestCase):
    '''
        python manage.py test transactions.tests.test_transaction_immutable.TransactionImmutableTestCase
    '''
    def test_create(self):
        """
        test that we can successfully create and store a new Transaction dataset
        """
        self.fail("not implemented")

    def test_change(self):
        """
        test that we cannot change a database-stored Transaction dataset
        """
        self.fail("not implemented")

    def test_delete(self):
        """
        test that we cannot delete a database-stored Transaction dataset
        """
        self.fail("not implemented")
