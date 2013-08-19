from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from zapisnici.models import Zapisnik

class IndexView(ListView):
    paginate_by = 10

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Zapisnik.objects.order_by('-zap_date')

class ZapisnikView(DetailView):
    model = Zapisnik

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DetailView, self).dispatch(*args, **kwargs)
