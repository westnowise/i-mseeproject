from django import forms
from .models import Account, Admin_account
from argon2 import PasswordHasher, exceptions

class RegisterForm(forms.ModelForm):
    userid = forms.CharField(
        label=' ',
        required= True,
        widget=forms.TextInput(
            attrs={
                'class' : 'userid',
                'size':'50',
                'placeholder' : 'ID'
            }
        ),
        error_messages={
            'required' : '아이디를 입력해주세요.',
            'unique' : '중복된 아이디입니다.'
            }
    )

    password = forms.CharField(
        label=' ',
        required= True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'password',
                'size':'50',
                'placeholder' : 'PW'
            }
        ),
        error_messages={'required' : '비밀번호를 입력해주세요.'}
    )

    password_confirm = forms.CharField(
        label=' ',
        required= True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'password_confirm',
                'size':'50',
                'placeholder' : 'checkPW'
            }
        ),
        error_messages={'required' : '비밀번호가 일치하지 않습니다.'}
    )
    name = forms.CharField(
        label=' ',
        required= True,
        widget=forms.TextInput(
            attrs={
                'class' : 'name',
                'size':'50',
                'placeholder' : 'NAME'
            }
        ),
        error_messages={'required' : '이름을 입력해주세요.'}
    )

    field_order = [
        'userid',
        'password',
        'password_confirm',
        'name',
    ]

    class Meta:
        model = Account
        fields = [
            'userid',
            'password',
            'name',
        ]

    def clean(self):
        cleaned_data = super().clean()

        userid = cleaned_data.get('userid','')
        password = cleaned_data.get('password','')
        password_confirm = cleaned_data.get('password_confirm','')
        name = cleaned_data.get('name','')

        if password != password_confirm:
            return self.add_error('password_confirm', '비밀번호가 다릅니다')
        else:
            self.userid = userid
            self.password = PasswordHasher().hash(password)
            self.password_confirm = password_confirm
            self.name = name

class LoginForm(forms.Form):
    userid = forms.CharField(
        max_length=25,
        label = ' ',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'userid',
                'size':'40',
                'placeholder':'id'
            }
        ),
        error_messages={'required' : '아이디를 입력하세요'}
    )
    password = forms.CharField(
        max_length=25,
        label=' ',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':'비밀번호',
                'size':'40',
                'placeholder':'password',
            }
        ),
        error_messages = {'required' : '비밀번호를 입력해주세요'}
    )

    field_order = [
        'userid',
        'password',
    ]

    def clean(self):
        cleaned_data = super().clean()

        userid = cleaned_data.get('userid', '')
        password = cleaned_data.get('password','')

        if userid == '':
            return self.add_error('userid', '아이디를 다시 입력해주세요')
        if password == '':
            return self.add_error('password', '비밀번호를 다시 입력해주세요')
        else:
            try:
                user = Account.objects.get(userid = userid)
            except Account.DoesNotExist:
                return self.add_error('userid', '아이디가 존재하지 않습니다')
            
            try:
                PasswordHasher().verify(user.password, password)
            except exceptions.VerifyMismatchError:
                return self.add_error('password', '비밀번호가 다릅니다.')
            
            self.login_session = user.userid
            self.userid = user.userid
            
            
            
class AdminRegisterForm(forms.ModelForm):
    userid = forms.CharField(
        label=' ',
        required= True,
        widget=forms.TextInput(
            attrs={
                'class' : 'userid',
                'size':'50',
                'placeholder' : 'ID'
            }
        ),
        error_messages={
            'required' : '아이디를 입력해주세요.',
            'unique' : '중복된 아이디입니다.'
            }
    )

    password = forms.CharField(
        label=' ',
        required= True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'password',
                'size':'50',
                'placeholder' : 'PW'
            }
        ),
        error_messages={'required' : '비밀번호를 입력해주세요.'}
    )

    password_confirm = forms.CharField(
        label=' ',
        required= True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'password_confirm',
                'size':'50',
                'placeholder' : 'checkPW'
            }
        ),
        error_messages={'required' : '비밀번호가 일치하지 않습니다.'}
    )
    name = forms.CharField(
        label=' ',
        required= True,
        widget=forms.TextInput(
            attrs={
                'class' : 'name',
                'size':'50',
                'placeholder' : 'NAME'
            }
        ),
        error_messages={'required' : '이름을 입력해주세요.'}
    )

    field_order = [
        'userid',
        'password',
        'password_confirm',
        'name'
    ]

    class Meta:
        model = Admin_account
        fields = [
            'userid',
            'password',
            'name',
            # 'is_staff',
        ]

    def clean(self):
        cleaned_data = super().clean()

        userid = cleaned_data.get('userid','')
        password = cleaned_data.get('password','')
        password_confirm = cleaned_data.get('password_confirm','')
        name = cleaned_data.get('name','')

        if password != password_confirm:
            return self.add_error('password_confirm', '비밀번호가 다릅니다')
        else:
            self.userid = userid
            self.password = PasswordHasher().hash(password)
            self.password_confirm = password_confirm
            self.name = name



class AdminLoginForm(forms.Form):
    userid = forms.CharField(
        max_length=25,
        label = ' ',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'userid',
                'size':'40',
                'placeholder':'id'
            }
        ),
        error_messages={'required' : '아이디를 입력하세요'}
    )
    password = forms.CharField(
        max_length=25,
        label=' ',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':'비밀번호',
                'size':'40',
                'placeholder':'password',
            }
        ),
        error_messages = {'required' : '비밀번호를 입력해주세요'}
    )

    field_order = [
        'userid',
        'password',
    ]

    def clean(self):
        cleaned_data = super().clean()

        userid = cleaned_data.get('userid', '')
        password = cleaned_data.get('password','')

        if userid == '':
            return self.add_error('userid', '아이디를 다시 입력해주세요')
        if password == '':
            return self.add_error('password', '비밀번호를 다시 입력해주세요')
        else:
            try:
                user = Admin_account.objects.get(userid = userid)
            except Admin_account.DoesNotExist:
                return self.add_error('userid', '아이디가 존재하지 않습니다')
            
            try:
                PasswordHasher().verify(user.password, password)
            except exceptions.VerifyMismatchError:
                return self.add_error('password', '비밀번호가 다릅니다.')
            
            self.login_session = user.userid