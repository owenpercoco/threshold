from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import PostForm


from .models import Post, Image, Category, Featured
from accounts.models import User_Group

# Create your views here.
def post_list(request):
    featured = Featured.objects.all()
    posts = Post.objects.exclude(id = featured.values('post_id')).filter(public=1).filter(published_date__lte=timezone.now()).order_by('-published_date')

    return render(request, 'blog/home.html', {'posts': posts, 'features': featured})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.group:
        users=post.group.users.all()
    else:
        users = post.author
    return render(request, 'blog/post_detail.html', {'post': post, 'users': users})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug=slugify(post.title)
            if post.public == 1:
                post.published_date = timezone.now()
            if form.cleaned_data.get('new_image') :
                image = Image(title=post.title, description=post.description, image = request.FILES['new_image'])
                image.save()
                post.image = image


            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(user=request.user)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)


    if post.can_edit(post, request.user) is True:
        if request.method == "POST":
            form = PostForm(request.user, request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                if post.public == 1:
                    post.published_date = timezone.now()
                if form.cleaned_data.get('new_image') :
                    image = Image(title=post.title, description=post.description, image = request.FILES['new_image'])
                    image.save()
                    post.image = image
                post.save()
                return redirect('post_detail', pk=post.pk)

        else:
            form = PostForm(instance=post, user=request.user)
    else:
        return redirect('post_list')
    return render(request, 'blog/post_edit.html', {'form': form})


# Heres our category list view
def category(request, slug):
    categoryObject = get_object_or_404(Category, slug=slug)
    pk = categoryObject.pk
    posts = Post.objects.filter(published_date__lte=timezone.now()).filter(category_id=pk).order_by('published_date')

    return render(request, 'blog/category.html', {'posts': posts})

