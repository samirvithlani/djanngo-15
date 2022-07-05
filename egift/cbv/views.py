from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView

from .models import Event, News


# Create your views here.
class NewsListView(ListView):
    model = News
    template_name = "news/news_list.html"
    context_object_name = "news_list"
    
class NewsCreateView(CreateView):
    model= News
    #fields = ['title','description','publishDate']
    fields = '__all__'
    template_name = "news/news_create.html"
    success_url = "/cbv/newslist/"

class NewsDetailView(DetailView):
    model = News
    template_name = "news/news_detail.html"
    context_object_name = "news_detail"    


class NewsDeleteView(DeleteView):
    model = News
    template_name = "news/news_delete.html"
    success_url = "/cbv/newslist/"
    
class EvenetCreateView(CreateView):
    model =Event
    template_name = "news/event.html"
    success_url ="/"
    fields = "__all__"
        