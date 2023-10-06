import random
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from main.users.forms import UserRegisterForm, UserProfileForm, EmailVerificationForm
from main.users.models import User, UserVerification


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def verify(request):
    if request.method == 'POST':
        verification_code = request.POST.get('verification_code')
        user_verification = UserVerification.objects.filter(
            user=request.user, verification_code=verification_code).first()
        if user_verification:
            user_verification.delete()
            request.user.is_verified = True
            request.user.save()
            messages.success(request, 'Email успешно подтвержден!')
            return redirect('/')
        else:
            messages.error(request, 'Неверный код подтверждения!')
    return render(request, 'verification/verify.html')


def send_verification_email(request):
    if request.method == 'POST':
        form = EmailVerificationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                verification_code = str(random.randint(100000, 999999))
                UserVerification.objects.create(
                    user=user, verification_code=verification_code)
                send_mail(
                    'Verification code',
                    f'Ваш код для авторизации {verification_code}',
                    'margoonavt@yandex.ru',
                    [email],
                    fail_silently=False,
                )
                return redirect('users:verify')
            except User.DoesNotExist:
                # Обработка, если пользователь не существует
                pass
    else:
        messages.error(request, 'Неверный код подтверждения!')
        form = EmailVerificationForm()
    return render(request,
                  'verification/send_verification_email.html',
                  {'form': form})
