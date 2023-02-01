from django.db import models

from django.contrib.auth.models import AbstractUser

## member Model
class Member(AbstractUser):
    ID = models.CharField("ID", max_length=20, primary_key=True)
    nickname = models.CharField("nickname", max_length=20, unique=True)
    email = models.CharField("email", max_length=50, null=False)
    email_cert = models.BooleanField("email_cert", default=False)  # 이메일 인증 여부
    denied = models.BooleanField("denied", default=False)  # 차단 여부
    joined_date = models.DateTimeField("joined_date")
    last_login = models.DateTimeField("last_login")

    USERNAME_FIELD = "ID"
    REQUIRED_FIELDS = []

    class Meta:
        managed = True
        db_table = "member"
