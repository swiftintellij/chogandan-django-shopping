from django import forms
from django.contrib.auth.hashers import check_password, make_password
from customer.models import Customer


class JoinForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            "required": "이메일을 입력해주세요."
        },
        max_length=64,
        label="이메일",
    )
    password = forms.CharField(
        error_messages={
            "required": "비밀번호를 입력해주세요."
        },
        widget=forms.PasswordInput,
        label="비밀번호",
    )
    confirm_password = forms.CharField(
        error_messages={
            "required": "비밀번호를 한번더 입력해주세요."
        },
        widget=forms.PasswordInput,
        label="비밀번호 다시입력",
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password:
            if password != confirm_password:
                error_msg = "입력한 비밀번호가 서로 다릅니다."
                self.add_error("password", error_msg)
                self.add_error("confirm_password", error_msg)


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            "required": "이메일을 입력해주세요."
        },
        max_length=64,
        label="이메일",
    )
    password = forms.CharField(
        error_messages={
            "required": "비밀번호를 입력해주세요."
        },
        widget=forms.PasswordInput,
        label="비밀번호",
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        email = cleaned_data.get("email")
        if email and password:
            try:
                customer = Customer.objects.get(email=email)
            except Customer.DoesNotExist:
                self.add_error("email", "아이디가 없습니다")
                return

            if not check_password(password, customer.password):
                self.add_error("password", "비밀번호가 틀렸습니다.")
            else:
                self.email = customer.email
