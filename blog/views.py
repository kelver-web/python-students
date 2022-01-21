from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.contrib import messages
from .models import Email
#from .forms import EmailForm


# Create your views here.


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/list.html'


'''def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/list.html', {'page': page, 'posts':posts})'''


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                              status='published',
                              publish__year=year,
                              publish__month=month,
                              publish__day=day)
    return render(request, 'blog/detail.html', {'post': post})


def about(request):
    return render(request, 'blog/about.html')


def zen_of_python(request):
    return render(request, 'blog/zen.html')


def sendd_email(request):
    
    if request.method == 'POST':
        email = request.POST.get('semail1')
        if email:
            messages.success(request, 'Seu email foi enviado com sucesso!')
            Email.objects.create(email=email)
        return redirect('/')
    
    return render(request, 'blog/list.html',)
