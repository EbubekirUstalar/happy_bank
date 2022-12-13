import factory
from factory import faker


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "transactions.Transaction"

    account = factory.SubFactory("bankaccounts.factories.BankAccountFactory")
    remote = factory.SubFactory("bankaccounts.factories.BankAccountFactory")
    value = faker.Faker("pyint", min_value=0, max_value=100000)
