from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .forms import ArticleForm
from .models import Article

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm

    

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return(get_object_or_404(Article,id=id_))


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return(get_object_or_404(Article,id=id_))

    