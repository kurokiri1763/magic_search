# Generated by Django 5.1.5 on 2025-02-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_alter_magic_effect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magic',
            name='effect',
            field=models.TextField(max_length=1000, verbose_name='効果'),
        ),
        migrations.AlterField(
            model_name='magic',
            name='extended_effect1',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='拡張効果1'),
        ),
        migrations.AlterField(
            model_name='magic',
            name='extended_effect2',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='拡張効果2'),
        ),
        migrations.AlterField(
            model_name='magic',
            name='magic_type',
            field=models.CharField(choices=[('sorcerer', '真語魔法'), ('conjurer', '操霊魔法'), ('wizard', '深智魔法'), ('priest', '基本神聖魔法'), ('unique_priest', '特殊神聖魔法'), ('magitech', '魔動機術'), ('fairy_tamer', '基本妖精魔法'), ('special_fairy_tamer', '特殊妖精魔法'), ('druid', '森羅魔法'), ('daemon_ruler', '召異魔法'), ('abyssgazer', '奈落魔法')], max_length=20, verbose_name='系統'),
        ),
    ]
