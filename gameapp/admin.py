from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')  # 一覧表示に表示するフィールド
    search_fields = ('name', 'description')  # 検索対象フィールド
