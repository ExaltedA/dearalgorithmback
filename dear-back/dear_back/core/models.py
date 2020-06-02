from django.db import models


class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    message = models.CharField(max_length=500)

    def datepublished(self):
        return self.date.strftime('%B %d %Y')
