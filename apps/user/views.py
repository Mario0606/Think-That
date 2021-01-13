from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from .models import User


class UserCreateView(CreateView):
    template_name = 'user/create_user.html'
    model = DjangoUser
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            User(user=user, profile_photo=form.cleaned_data.get('profile_photo')).save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
        return redirect(reverse_lazy('create_user'))
