from django.db import models
from user_auth.models import User

class Connection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.TextField(max_length=512)
    domain = models.URLField()
    permission = models.JSONField(null=True)

class PermissionLink(models.Model):
    link = models.URLField()
    domain = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    