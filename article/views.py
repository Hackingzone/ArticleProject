from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView ,CreateView# new
from django.urls import reverse_lazy # new
from .models import Article

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'article_matter/article_new.html'
    fields = ('title', 'body') 
    login_url='login'
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

from .models import Article
class ArticleListView(ListView):
    model = Article
    template_name = 'article_matter/article_list.html'
class ArticleDetailView(DetailView): 
    model = Article
    template_name = 'article_matter/article_detail.html'
class ArticleUpdateView(UpdateView): 
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_matter/article_edit.html'
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_matter/article_delete.html'
    success_url = reverse_lazy('article_list')

    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)