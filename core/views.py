from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from core import forms


class RegistrationSucceedTemplateView(TemplateView):
    template_name = 'registration_succeed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context


class IndexCreateView(CreateView):
    template_name = 'index.html'
    form_class = forms.UserProfileModelForm
    success_url = reverse_lazy('registration_succeed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context
