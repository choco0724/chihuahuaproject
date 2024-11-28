# chihuapp/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['username'] = self.request.user.username  # カスタムフィールドの場合は.nickname
        return context