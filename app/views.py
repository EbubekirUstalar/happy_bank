from django.views.generic import RedirectView


class IndexView(RedirectView):
    permanent = True
    url = "/onlinebanking/"
