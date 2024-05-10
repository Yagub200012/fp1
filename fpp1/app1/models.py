from django.db import models


class Stage(models.Model):
    other_model = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=3000)
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Stage'
        verbose_name_plural = 'Stages'

