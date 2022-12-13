from django.urls import path

from onlinebanking.views import TransactionsListView, WelcomeView, create_transaction

urlpatterns = [
    path("", WelcomeView.as_view(), name="onlinebanking-welcome"),
    path(
        "transactions/",
        TransactionsListView.as_view(),
        name="onlinebanking-transaction-list",
    ),
    path("create_transaction/", create_transaction, name="create-transaction"),
]
