from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from accounts.forms import BaseModelForm
from .models import Post



class PostForm(BaseModelForm):
    new_image = forms.ImageField(required=False)
    #GROUPS = user.groups.all()
    group = forms.ModelChoiceField(queryset='', required = False)

    def __init__(self,user, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['group'].queryset = user.user_groups.all()

    class Meta:
        model = Post
        fields = ('title','category', 'group', 'text', 'image', 'new_image', 'public', 'description', 'style')

        help_texts = {
            'public': _('check this if you\'re ready to go public and publish your work, otherwise no one can see it but you.'),
            'new_image': _('either upload a new image, or choose from the gallery'),
            'group': _('Do you want this published under your account or a group?')
        }

