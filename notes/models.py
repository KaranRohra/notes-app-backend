from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
