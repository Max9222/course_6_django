import random
import secrets

from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView, UpdateView, DeleteView

from users.forms import UserRegisterForm, UserForm
from users.models import User
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render
from users.services import send_verify_code, send_password

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required


class LoginView(BaseLoginView):
    template_name = 'users/login.html'

class LogoutView(BaseLogoutView):
    template_name = 'users/logout.html'

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:verify_email', args=['code'])
    template_name = 'users/register.html'

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            code = secrets.token_urlsafe(nbytes=8)
            new_user.verify_code = code
            new_user.save()
            url_email = self.request.build_absolute_uri(reverse('users:verify_email', args=[code]))
            send_verify_code(new_user, url_email)
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user

class ProfileDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('users:register')

# @login_required
def verify(request, code):
    try:
        user = User.objects.get(verify_code=code)
        user.is_active = True
        user.save()
        return redirect(reverse('users:login'))
    except User.DoesNotExist:
        return render(request, 'users/verify.html')

# @login_required
def gen_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        send_password(user.email, new_password)
        user.set_password(new_password)
        user.save()
        return redirect(reverse('users:login'))
    return render(request, 'users/password.html')
