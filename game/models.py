from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=100)
    group = models.IntegerField()
    solution_name = models.CharField(max_length=100)

    def __str__(self):
        return self.text

class GameState(models.Model):
    cards = models.JSONField(default=list)
    timer_started_at = models.DateTimeField(null=True, blank=True)
    timer_stopped = models.BooleanField(default=False)