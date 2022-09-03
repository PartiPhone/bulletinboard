from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from .models import AdvUser
from .forms import ChangeUserInfoForm


def index(request):
    return render(request, 'main/index.html')
    
def other_page(request, page):
    try:
        print(page)
        template = get_template('main/'+ page +'.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))
    
class BBLoginView(LoginView):
    template_name = 'main/login.html'
    
class ChangeUserInfo(SuccessMessageMixin, UpdateView):
    model = AdvUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('main:profile')
    success_message = 'Данные пользователя изменены'
    
    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)
    
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)
    

