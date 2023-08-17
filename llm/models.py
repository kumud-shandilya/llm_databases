from django.db import models

class UserPrompt(models.Model):
    user_query = models.CharField(max_length=10000)
    table_name = models.CharField(max_length=10000)

