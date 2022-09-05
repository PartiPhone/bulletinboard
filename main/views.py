from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, \
                                    PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib import messages

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

@login_required
def profile(request):
    return render(request, 'main/profile.html')
    
class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'

class BBPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin,
                                PasswordChangeView):
    template_name = 'main/change_password.html'
    success_url = reverse_lazy('main:profile')
    success_message = 'Пароль пользователя изменён'
    
class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'main/delete_user.html'
    success_url = reverse_lazy('main:index')
    
    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS,
                                'Пользователь удален')
        return super().post(request, *args, **kwargs)
        
    def get_object(self, queryset=None):
        if not self.queryset:
            queryset = self.get_queryset()
            return get_object_or_404(queryset, pk=self.user_id)


