from django.urls import path
from .views import ContactView, SuccessView

app_name = "contact"

urlpatterns = [
    path("", ContactView.as_view(), name="form"),  # 問い合わせフォームページ
    path("success/", SuccessView.as_view(), name="success"),  # 問い合わせ送信成功ページ
]
