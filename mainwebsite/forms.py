from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as DjangoUser


class CreateUserForm(UserCreationForm):
    class Meta:
        model = DjangoUser
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control',
                                                     'aria-describedby': 'inputGroup-sizing-default',
                                                     'placeholder': 'username',
                                                     'style': 'text-align: center'})

        self.fields['password1'].widget.attrs.update({'class': 'form-control',
                                                      'aria-describedby': 'inputGroup-sizing-default',
                                                      'placeholder': 'password',
                                                      'style': 'text-align: center'})

        self.fields['password2'].widget.attrs.update({'class': 'form-control',
                                                      'aria-describedby': 'inputGroup-sizing-default',
                                                      'placeholder': 'confirm password',
                                                      'style': 'text-align: center'})
