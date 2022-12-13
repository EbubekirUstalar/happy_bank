import factory
from factory import faker


class BankAccountOwnerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "bankaccounts.BankAccountOwner"

    given_name = faker.Faker("first_name")
    family_name = faker.Faker("last_name")
    email = faker.Faker("email")


class BankAccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "bankaccounts.BankAccount"

    owner = factory.SubFactory("bankaccounts.factories.BankAccountOwnerFactory")
    iban = faker.Faker("iban")
    balance = faker.Faker("pyint", min_value=0, max_value=100000)
