from django.db import models

# Create your models here.


class Content(models.Model):
    article_title = models.TextField()
    article_description = models.TextField()
    article_body = models.TextField()
    article_author = models.CharField(max_length = 50)
    article_image_link = models.TextField()

    def __str__(self):
        return self.article_title + ' ' + self.article_author + ' ' + str(self.id)