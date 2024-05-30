from django.db import models
import hashlib


class Stage(models.Model):
    title = models.CharField(max_length=3000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Stage'
        verbose_name_plural = 'Stages'


class Subtage(models.Model):
    mainstage = models.ForeignKey(Stage, verbose_name="Main stage", related_name='substage_set', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=3000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Subtage'
        verbose_name_plural = 'Subtages'


class Question(models.Model):
    stage = models.ForeignKey(Subtage, verbose_name="Subtage link", related_name='question_set', on_delete=models.CASCADE)
    question_text = models.TextField()

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, verbose_name="Question link", related_name='answer_set', on_delete=models.CASCADE)
    answer_text = models.TextField()
    answer_hash = models.TextField(blank=True, editable=False)

    def save(self, *args, **kwargs):
        if self.answer_text:
            hash_object = hashlib.sha256(self.answer_text.encode('utf-8'))
            self.answer_hash = hash_object.hexdigest()
        super(Answer, self).save(*args, **kwargs)






