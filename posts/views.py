from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Count, Q
from .models import Post, Author, Comment, PostView
from .forms import CommentForm, PostForm

# Create your views here.

def get_user(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def get_category_count():
    queryset = Post.objects.values(
        'category__name').annotate(Count('category__name'))
    return queryset

# def get_author_count():
# 	queryset = Post.objects.values('author__content').annotate(Count('author__content'))
# 	return queryset

def search(request):
    queryset = Post.objects.all()
    query    = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains = query) | 
            Q(overview__icontains = query)
        ).distinct()
        context = {'queryset': queryset}
        return render(request, 'search_result.html', context)

def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def service(request):
    return render(request, 'service.html', {})

# def get_author():
#     get_author_query = Post.objects.values('author')


def post(request):
    posts = Post.objects.order_by('-title')
    cat_queryset = get_category_count()
    # get_author_query = get_author()
    
    context = {
        'posts': posts,
        'cat_queryset': cat_queryset,
        # 'get_author_query': get_author_query
    }
    return render(request, 'blog.html', context)


def single_post(request, id):  
    post = get_object_or_404(Post, id=id)
    # comments = Comment.objects.order_by('-timestamp')
    
    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user,  post=post)

    if request.method == 'POST':
        
        form = CommentForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            
            return redirect(reverse('post_details', kwargs={
                'id': post.id
            }))
    else:
        form = CommentForm()
        
    context = {
        'post': post,
        # 'comments': comments,
        'form' : form,
    }
    return render(request, 'single-post.html', context)


def contact(request):
    return render(request, 'contact.html', {})

def create(request):
    title = 'Create'
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_user(request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            
            return redirect(reverse('post_details', kwargs={
                'id': form.instance.id
            }))
    else:
        form = PostForm()
    
    context = {
        'form' : form,
        'title' : title,
    }

    return render(request, 'create_post.html', context)

def post_update(request, id):
    title = 'Update'
    post = get_object_or_404(Post, pk=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    author  = get_user(request.user)
    if request.method =='POST':
        if form.is_valid():
            form.instance.author = author
            form.save() 
            
            return redirect(reverse('post_details', kwargs={
                'id': form.instance.id
            }))
    else:
        form = PostForm()
    
    context = {
        'form' : form,
        'title' : title,
    }

    return render(request, 'create_post.html', context)
    

def post_delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()

    return redirect(reverse('posts'))