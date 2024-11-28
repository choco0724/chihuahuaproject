from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chihuapp.urls')),  # chihuappのURLを含む
    path('accounts/', include('accounts.urls')),
    path('games/', include('gameapp.urls')),  # gameappのURLを含む
    path('contact/', include('contactapp.urls')),  # contactappのURLを含む
]

# メディアファイル（画像やZIPファイル）へのアクセスを提供
if settings.DEBUG:  # 開発環境のみで適用
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
