from django.forms import ModelForm, CharField
from .models import Transaction
from django.core.exceptions import ValidationError


def validate_value(value):
    if value == "0":
        raise ValidationError(
            '%(value)s cannot be used',
            params={'value': value},
        )


class TransactionForm(ModelForm):
    value = CharField(validators=[validate_value])

    class Meta:
        model = Transaction
        fields = ["account", "value"]


