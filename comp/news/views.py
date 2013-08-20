from django.http import HttpResponse
from news.models import News
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    paginate_by = 10

    def get_queryset(self):
        return News.objects.order_by('date')

class NewsView(generic.DetailView):
    model = News
