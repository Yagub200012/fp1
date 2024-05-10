from django.db import models


class Stage(models.Model):
    other_model = models.ForeignKey('self', verbose_name="Main stage link", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=3000)
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Stage'
        verbose_name_plural = 'Stages'



