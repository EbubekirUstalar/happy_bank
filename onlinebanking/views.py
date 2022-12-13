from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from transactions.models import Transaction
from transactions.forms import TransactionForm


class WelcomeView(TemplateView):
    template_name = "onlinebanking/welcome.html"


class TransactionsListView(ListView):
    model = Transaction
    template_name = "onlinebanking/transactions.html"
    context_object_name = 'transactions'
    paginate_by = 25

    def get_queryset(self):
        queryset = Transaction.objects.filter(account__owner__email__icontains="@").order_by('-value',)
        return queryset


def create_transaction(request):
    form = TransactionForm()
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/onlinebanking/transactions/')
    context = {'form': form}
    return render(request, "onlinebanking/create_transaction.html", context)
