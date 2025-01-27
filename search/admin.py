from django.contrib import admin
from .models import Magic

@admin.register(Magic)
class MagicAdmin(admin.ModelAdmin):
    list_display = ('name', 'magic_type', 'rank', 'target', 'range_shape') # 管理画面に表示するフィールド
    list_filter = ('name','magic_type','rank','attribute',) # 検索時のフィルター
    search_fields = ('name','magic_type', 'rank','attribute',) # 検索可能なフィールド
    ordering = ('rank','name',) #並び順の設定

    def get_magic_type(self, obj):
        return obj.get_magic_type_display()
    get_magic_type.short_description = '魔法の系統'
