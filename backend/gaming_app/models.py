from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name}"