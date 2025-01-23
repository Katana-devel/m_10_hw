from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Quote, Author
from .forms import AddAuthorForm, AddQuoteForm


def index(request):
    quotes = Quote.objects.select_related('author').all()
    return render(request, 'index.html', {'quotes': quotes})


def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_quotes:home')  # Перенаправляем на домашнюю страницу
    else:
        form = AddAuthorForm()
    return render(request, 'add_author.html', {'form': form})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = AddQuoteForm(request.POST)
        if form.is_valid():
            # Сохраняем цитату с привязкой к текущему пользователю
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            return redirect('add_quotes:home')  # Перенаправляем на домашнюю страницу
    else:
        form = AddQuoteForm()

    # Передаем список авторов в шаблон
    authors = Author.objects.all()
    return render(request, 'upend_quotes.html', {'form': form, 'authors': authors})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'add_quotes/author_detail.html', {'author': author})
