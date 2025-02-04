from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse


class HomepageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'the Most Esteemed Visitor'
        return context


def home_redirect(request):
    return redirect(reverse('article', args=['python', 42]))


def about(request):
    return render(request, 'about.html')
