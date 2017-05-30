from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm, EditProfileForm, AvatarForm, GroupForm, addtoGroupForm
from django.utils import timezone
from django.contrib.auth.models import User
from .models import User_Group, Profile, Avatar
from blog.models import Post
from .decorators import check_recaptcha

@check_recaptcha
def profile_new(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid() and request.recaptcha_is_valid:
            user = user_form.save(commit=False)
            profile = profile_form.save(commit=False)
            user.username = user.email
            user.set_password(user.password)
            user.save()
            profile.user = user
            profile.display_name = user.first_name +' '+ user.last_name
            profile.slug = slugify(profile.display_name)

            if profile_form.cleaned_data.get('new_image') :
                avatar = Avatar(user=user, title=user.first_name, description=user.email, image = request.FILES['new_image'])
                avatar.save()
                profile.avatar = avatar

            profile.save()
            login(request, user)
            return redirect('profile_detail', pk=user.pk)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'accounts/update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def update_profile(request):
    if request.method == 'POST':
        profile_form = EditProfileForm(request.POST, instance=request.user.profile)
        if  profile_form.is_valid():
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('/')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        profile_form = EditProfileForm(instance=request.user.profile)
    return render(request, 'accounts/update.html', {
        'profile_form': profile_form
    })

@login_required
def new_group(request):
    if request.method == 'POST':
        group_form = GroupForm(request.POST)
        if group_form.is_valid():
            group = group_form.save(commit=False)
            group.slug = slugify(group.name)
            group.save()
            group.users.add(request.user)
            group.save()
            return redirect('group_detail', slug=group.slug)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        group_form = GroupForm()
    return render(request, 'accounts/group_update.html', {
        'group_form': group_form
    })

@login_required
def update_avatar(request):
    if request.method == 'POST':
        avatar_form = AvatarForm(request.POST, request.FILES)
        if avatar_form.is_valid():
            avatar = avatar_form.save(commit=False)
            avatar.user = request.user
            avatar.save()
            profile = request.user.profile
            profile.avatar = avatar
            profile.save()
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        avatar_form = AvatarForm()
    return render(request, 'accounts/avatar_update.html', {
        'avatar_form': avatar_form
    })

def profile_detail(request, pk='', slug=''):
    if pk == '' and slug == '':
        if not request.user.is_authenticated():
            messages.error(request, ('You don\'t have an account, or you need to login'))
            return redirect(auth_views.login)
        profile = request.user
        my_account = True
        posts = Post.objects.filter(author=request.user).order_by('created_date')

    elif slug == '':
        profile = get_object_or_404(User, pk=pk)
        my_account = False
        posts = Post.objects.filter(author=profile).filter(public=1).filter(published_date__lte=timezone.now()).order_by('-published_date')
    elif pk == '':
        pro = get_object_or_404(Profile, slug=slug)
        profile = get_object_or_404(User, pk=pro.user_id)
        my_account = False
        posts = Post.objects.filter(author=profile).filter(public=1).filter(published_date__lte=timezone.now()).order_by('-published_date')

    if request.method == "POST":
        form = addtoGroupForm(request.user, profile.pk, request.POST)
        if form.is_valid():
            form.save(commit = False)
            Group = form.cleaned_data.get('user_group')
            Group.users.add(form.cleaned_data.get('add_user'))
            Group.save()

    else:
        form = addtoGroupForm(request.user, profile.pk)


    return render(request, 'accounts/profile.html', {'user': profile, 'posts':posts, 'My_Account':my_account, 'form':form})

def group_detail(request, pk='', slug=''):
    if slug == '':
        group = get_object_or_404(User_Group, pk=pk)
    elif pk == '':
        group = get_object_or_404(User_Group, slug=slug)
    elif pk == '' and slug == '':
        messages.success(request, ('What are you looking for?'))
        return redirect('/')

    users = group.users.all()
    if request.user in users:
        post = Post.objects.filter(group=group.id).order_by('-created_date')
    else:
        post = Post.objects.filter(group=group.id).filter(public=1).filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'accounts/group-profile.html', {'group': group, 'users':users, 'posts':post})

