from django.db import models
from django.utils import timezone
from enum import Enum
from model_utils import Choices
from django.contrib.auth.models import AbstractUser
from users.models import User

# class Status(AbstractUser):
# 	waiting ='wt'
# 	working ='wa'
# 	done = 'dn'
#
#
#
# 	choose =[
# 		(waiting, 'waiting'),
# 		(working, 'working'),
# 		(done, 'done'),
# 	]
# 	Choose = models.CharField(max_length=15,choices=choose)


class TodoList(models.Model):
    waiting = 'wt'
    working = 'wa'
    done = 'dn'

    choose = Choices(
        (waiting, 'waiting'),
        (working, 'working'),
        (done, 'done'),
    )
    Choose = models.CharField(max_length=15, choices=choose, default=choose.wt)

    id_no = models.IntegerField()
    title = models.CharField(max_length=250)
    discription = models.TextField(max_length=200, blank=True)
    created_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    user = models.ForeignKey(User,related_name= 'todos',on_delete=models.CASCADE)

    class Meta:
        ordering = ["-id_no"]

    def __str__(self):
        return self.title
