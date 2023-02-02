from django.db import models

from django.contrib.auth.models import AbstractUser

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


## room Model
# 필드에 PK를 선언하지 않는다면 id필드가 자동적으로 생성되며 autoIncrease가 적용된다
class Room(models.Model):
    room_name = models.CharField("room_name", max_length=10, unique=True)

    class Meta:
        managed = True
        db_table = "Room"


## Chat Log
class ChatLog(models.Model):
    user = models.ForeignKey("Member", on_delete=models.DO_NOTHING)
    chat_txt = models.CharField("chat_txt", max_length=256)
    chat_time = models.DateTimeField("chat_time")

    class Meta:
        managed = True
        db_table = "Chat_Log"
