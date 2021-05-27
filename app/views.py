from .forms import MyForm
from django.shortcuts import render
from django.contrib import messages
def home(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Success!')
        else:
            messages.error(request, 'Wrong Captcha!')
    form = MyForm()
    return render(request, 'home.html', {'form': form})