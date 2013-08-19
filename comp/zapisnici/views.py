from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from zapisnici.models import Zapisnik

@login_required
def index(request):
    template = 'zapisnici/index.html'
    zapisnici_list = Zapisnik.objects.order_by('-zap_date')
    paginator = Paginator(zapisnici_list, 10)
    page = request.GET.get('page')
    try:
        zapisnici = paginator.page(page)
    except PageNotAnInteger:
        zapisnici = paginator.page(1)
    except EmptyPage:
        zapisnici = paginator.page(paginator.num_pages)

    return render(request, template, {'zapisnik_list': zapisnici})

@login_required
def detail(request, pk):
    context = {'zapisnik': get_object_or_404(Zapisnik, pk=pk)}
    template = 'zapisnici/detail.html'
    return render(request, template, context)
