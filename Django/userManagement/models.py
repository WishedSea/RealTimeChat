from django.contrib.auth.models import AbstractUser
from django.db import models

## member Model
class Member(AbstractUser):
    first_name = None
    last_name = None

    ID = models.CharField("ID", max_length=20, primary_key=True)
    username = models.CharField("nickname", max_length=100, unique=True)
    email = models.CharField("email", max_length=50, null=False, unique=True)
    email_cert = models.BooleanField("email_cert", default=False)  # 이메일 인증 여부
    last_login = models.DateTimeField("last_login")
    expired = models.BooleanField("expired", default=False)
    expire_date = models.DateTimeField("expire_date", null=True)

    USERNAME_FIELD = "ID"
    REQUIRED_FIELDS = []

    class Meta:
        managed = True
        db_table = "Member"
