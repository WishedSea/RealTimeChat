from django.db import models

## room Model
# 필드에 PK를 선언하지 않는다면 id필드가 자동적으로 생성되며 autoIncrease가 적용된다
class Room(models.Model):
    room_name = models.CharField("room_name", max_length=10, unique=True)

    class Meta:
        managed = True
        db_table = "Room"


## Chat Log
class ChatLog(models.Model):
    user = models.ForeignKey("userManagement.Member", on_delete=models.DO_NOTHING)
    chat_txt = models.CharField("chat_txt", max_length=256)
    chat_time = models.DateTimeField("chat_time")

    class Meta:
        managed = True
        db_table = "Chat_Log"
