from django.shortcuts import render
from django.views.generic import TemplateView, ListView

class MainPageView(TemplateView):
    template_name="pages/main.html"

main_page_view=MainPageView.as_view()