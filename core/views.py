from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


def frontpage(request):
    return render(request, 'core/frontpage.html')


def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    context['form'] = form
    return render(request, 'core/signup.html', context)

