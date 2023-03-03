from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from main.apps import user_registered

User = get_user_model()


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Адрес электронной почты')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'notify',)


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(
        required=True, widget=forms.EmailInput, label='Адрес электронной почты'
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput, label='Пароль',
        help_text=password_validation.password_validators_help_text_html()
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput, label='Пароль (повторно)',
        help_text='Повторите пароль'
    )

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        try:
            password_validation.validate_password(password1)
        except ValidationError as error:
            self.add_error('password1', error)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'Введенные пароли не совпадают', code='password_mismatch'
            )}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()
        user_registered.send(self.__class__, instance=user)
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name',
                  'last_name', 'notify')
