from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100, verbose_name='ゲーム名')  # ゲームの名前
    description = models.TextField(verbose_name='詳細コメント')  # 詳細な説明
    thumbnail = models.ImageField(upload_to='thumbnails/', verbose_name='サムネイル')  # サムネイル画像
    file = models.FileField(upload_to='game_files/', verbose_name='ゲームファイル')  # ゲームファイル
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')  # 作成日時
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')  # 更新日時

    def __str__(self):
        return self.name  # 管理画面で表示される名前
