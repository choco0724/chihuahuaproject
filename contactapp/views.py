from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


class ContactView(FormView):
    template_name = "contactapp/contact.html"  # 問い合わせフォームのテンプレート
    form_class = ContactForm  # 使用するフォーム
    success_url = reverse_lazy("contact:success")  # 成功時のリダイレクト先

    def form_valid(self, form):
        # フォームが有効な場合にメールを送信
        subject = form.cleaned_data['subject']  # 件名
        message = form.cleaned_data['message']  # メッセージ
        email = form.cleaned_data['email']  # 送信者のメールアドレス
        send_mail(
            subject,
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL],  # 受信者のメールアドレス
            fail_silently=False,  # エラー時に例外を発生させる
        )
        return super().form_valid(form)  # デフォルトの処理を実行


class SuccessView(TemplateView):
    template_name = "contactapp/success.html"  # 問い合わせ成功時のテンプレート
