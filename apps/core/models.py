from django.db import models


class BlogRoll(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(verify_exists=False)
    order = models.SmallIntegerField(default=5)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('order',)