from django import forms
from django.core.exceptions import ValidationError
from .models import User, Profile, Avatar, User_Group

class BaseModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BaseModelForm, self).__init__(*args, **kwargs)
        # add common css classes to all widgets
        for field in iter(self.fields):
            #get current classes from Meta
            classes = self.fields[field].widget.attrs.get("class")
            if classes is not None:
                classes += " form-control"
            else:
                classes = "form-control"
            self.fields[field].widget.attrs.update({
                'class': classes
            })

class UserForm(BaseModelForm):
    confirm_password = forms.CharField(
        label="Confirm Password",
        required=True,
        widget=forms.PasswordInput()
        )


    def clean(self):

        if (self.cleaned_data.get('password') !=
            self.cleaned_data.get('confirm_password')):

            raise ValidationError(
                "Password and confirm password must match."
            )

        return self.cleaned_data
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(),
        }



class ProfileForm(BaseModelForm):
    new_image = forms.ImageField(required=True)
    class Meta:
        model = Profile
        fields = ('bio',  'location', 'new_image')

class EditProfileForm(BaseModelForm):
    class Meta:
        model = Profile
        fields = ('bio',  'location')

class AvatarForm(BaseModelForm):
    class Meta:
        model = Avatar
        fields = ('title',  'description', 'image')

class GroupForm(BaseModelForm):
    class Meta:
        model = User_Group
        fields = ('name', 'bio', 'public')

class addtoGroupForm(BaseModelForm):
    user_group = forms.ModelChoiceField(queryset='')
    add_user = forms.IntegerField()
    def __init__(self,user,add_user, *args, **kwargs):
        super(addtoGroupForm, self).__init__(*args, **kwargs)
        self.fields['user_group'].queryset = user.user_groups.all()
        self.fields['add_user'] = forms.IntegerField(label="", widget=forms.HiddenInput(attrs={'value':add_user}))
    class Meta:
        model = User_Group
        fields = ('user_group', 'add_user')

