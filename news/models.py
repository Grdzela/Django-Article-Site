from django.db import models


class Articles(models.Model):
    title = models.CharField('Satauri', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Statia')
    date = models.DateTimeField('Damatebis Tarigi')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
