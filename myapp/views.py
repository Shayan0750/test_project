from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import NewsArticle, Category
from .forms import NewsArticleForm
from django.http import HttpResponseForbidden,JsonResponse, Http404
from django.utils.html import escape



# Create your views here.

def home(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def categories_processor(request):
    return {
        'categories': Category.objects.all()
    }


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'حساب کاربری شما با موفقیت ایجاد شد!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def article_create(request):
    if request.method == 'POST':
        form = NewsArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail', article.id)
    else:
        form = NewsArticleForm()
    return render(request, 'articles/article_form.html', {'form': form})


@login_required
def article_edit(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)

    # Only allow the author or admin to edit
    if request.user != article.author and not request.user.is_staff:
        return redirect('article_detail', article.id)

    if request.method == 'POST':
        form = NewsArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', article.id)
    else:
        form = NewsArticleForm(instance=article)
    return render(request, 'articles/article_form.html', {'form': form})

def article_detail(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})

def article_list(request):
    articles = NewsArticle.objects.order_by('-created_at')  # newest first
    return render(request, 'articles/article_list.html', {'articles': articles})


@login_required
def article_delete(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)

    # Allow only the author or superuser (admin) to delete
    if request.user != article.author and not request.user.is_superuser:
        return HttpResponseForbidden("شما اجازه حذف این مقاله را ندارید.")

    if request.method == 'POST':
        article.delete()
        return redirect('article_list')  # after deletion go back to article list

    return render(request, 'articles/article_confirm_delete.html', {'article': article})


def article_detail_ajax(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    content = escape(article.content).replace('\n', '<br>')
    return JsonResponse({'content': content})

def articles_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = NewsArticle.objects.filter(category=category)
    return render(request, 'articles/articles_by_category.html', {
        'category': category,
        'articles': articles
    })