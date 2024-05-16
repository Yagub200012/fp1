from django.db import models
import hashlib


class Stage(models.Model):
    other_model = models.ForeignKey('self', verbose_name="Main stage link", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=3000)
    # question = models.TextField(blank=True, null=True)
    # answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Stage'
        verbose_name_plural = 'Stages'


class Question(models.Model):
    stage = models.ForeignKey(Stage, verbose_name="Stage link", on_delete=models.CASCADE)
    question_text = models.TextField()

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, verbose_name="Question link", on_delete=models.CASCADE)
    answer_text = models.TextField()
    answer_hash = models.TextField(blank=True, editable=False)

    def save(self, *args, **kwargs):
        if self.answer_text:
            hash_object = hashlib.sha256(self.answer_text.encode('utf-8'))
            self.answer_hash = hash_object.hexdigest()
        super(Answer, self).save(*args, **kwargs)






