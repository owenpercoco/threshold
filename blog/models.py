from django.db import models
from django.utils import timezone
from django.conf import settings

class Image(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/', default = 'images/None/no-img.jpg')
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100, null=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.slug

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='author')
    group = models.ForeignKey('accounts.User_Group', blank=True, null=True, related_name='group', on_delete=models.SET_NULL)
    editors = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='editors')
    group_edit = models.BooleanField(default=False)
    category = models.ForeignKey(Category)
    image = models.ForeignKey(Image, null=True, blank=True)
    style = models.ForeignKey('style.Colors', null=True)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank = True)
    text = models.TextField()
    is_front_page = models.BooleanField(default=False)
    public = models.BooleanField(default=False)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def can_edit(self, post, user):
        if post.author == user:
            return True
        elif user in post.editors.all():
            return True
        if post.group_edit is True:
            if user in post.group.users.all():
                return True
        return False
    def __str__(self):
        return self.title

class Featured(models.Model):
    post = models.ForeignKey(Post, related_name='post')





