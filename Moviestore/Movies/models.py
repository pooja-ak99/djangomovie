from django.db import models

class movie(models.Model):
    title = models.TextField(max_length=50)
    year = models.IntegerField()
    about = models.CharField(max_length=30)
    cover = models.ImageField(upload_to="movie/cover", null=True, blank=True)

    def __str__(self):
        return self.title
