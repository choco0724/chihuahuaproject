from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="お名前",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'お名前を入力してください'
        })
    )
    email = forms.EmailField(
        label="メールアドレス",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'メールアドレスを入力してください'
        })
    )
    subject = forms.CharField(  # subjectフィールドを追加
        max_length=100,
        label="件名",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '件名を入力してください'
        })
    )
    message = forms.CharField(
        label="メッセージ",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'メッセージを入力してください',
            'rows': 5,
        })
    )

