from django.contrib.auth.models import AbstractUser
from django.db import models

def user_icon_path(instance, filename):
    # ファイルの保存先を指定 (ユーザーごとに固有のディレクトリに保存)
    return f"user_icons/{instance.username}/{filename}"

class CustomUser(AbstractUser):
    """
    ユーザーモデルを拡張してアイコン画像を追加
    """
    icon = models.ImageField(
        upload_to=user_icon_path,  # アイコン画像のアップロード先
        blank=True,
        null=True,
        verbose_name="ユーザーアイコン"
    )

    def __str__(self):
        return self.username
