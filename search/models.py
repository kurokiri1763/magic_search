from django.db import models

class Magic(models.Model):
    """
    魔法の基本モデル
    """
    MAGIC_TYPES = [
        ('sorcerer', '真語魔法'),
        ('conjurer', '操霊魔法'),
        ('wizard','深智魔法'),
        ('priest', '基本神聖魔法'),
        ('unique_priest', '特殊神聖魔法'),
        ('magitech', '魔動機術'),
        ('fairy_tamer', '基本妖精魔法'),
        ('special_fairy_tamer', '特殊妖精魔法'),
        ('druid', '森羅魔法'),
        ('daemon_ruler', '召異魔法'),
        ('abyssgazer', '奈落魔法'),
    ]

    RESIST_CHOICES = [
        ('hit','必中'),
        ('optionally','任意'),
        ('none','なし'),
        ('negate', '消滅'),
        ('reduce', '半減'),
        ('shorten', '短縮'),
    ]

    name = models.CharField(max_length=100, verbose_name="名前")
    magic_type = models.CharField(max_length=20, choices=MAGIC_TYPES, verbose_name="系統")
    rank = models.IntegerField(verbose_name="魔法ランク")
    target = models.CharField(max_length=100, verbose_name="対象")
    range_shape = models.CharField(max_length=100, verbose_name="射程/形状")
    resistance = models.CharField(max_length=10, choices=RESIST_CHOICES, verbose_name="抵抗")
    duration = models.CharField(max_length=50, verbose_name="時間")
    cost = models.CharField(max_length=100, verbose_name="消費")
    summary = models.TextField(verbose_name="概要")
    attribute = models.CharField(max_length=50, verbose_name="属性", blank=True, null=True)
    effect = models.TextField(max_length=1000,verbose_name="効果")
    extended_effect1 = models.TextField(max_length=1000,verbose_name="拡張効果1", blank=True, null=True)
    extended_effect2 = models.TextField(max_length=1000,verbose_name="拡張効果2", blank=True, null=True)
    spell = models.TextField(max_length=100, verbose_name="詠唱", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    def __str__(self):
        return f"{self.name} ({self.get_magic_type_display()})"

    class Meta:
        ordering = ['rank', 'name']
        verbose_name = "魔法"
        verbose_name_plural = "魔法一覧"