from django.shortcuts import render, redirect
from .models import Post
from .forms import ContactForm


def news(request):
    data = {}
    data["dataset"] = Post.objects.all()
    return render(request, 'news.html', context=data)


def contact(request):
    if request.method == 'GET':
        context = {'form': ContactForm()}
        return render(request, 'contact.html', context)
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'contact.html', {'form': form})


def home(request):
    return render(request, 'home.html')
