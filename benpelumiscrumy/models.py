from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class GoalStatus(models.Model):
    status_name = models.CharField(max_length = 250)

    def __str__(self):
        return self.status_name    

class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length = 250)
    goal_id = models.IntegerField( default = 1, unique=True)
    created_by = models.CharField(max_length = 150)
    moved_by = models.CharField(max_length = 150)
    owner = models.CharField(max_length = 150)
    goal_status = models.ForeignKey(
        GoalStatus,
        on_delete = models.PROTECT,
        related_name = 'scrumy_goal'
    ) 
    user = models.ForeignKey(
        User,
        related_name = 'scrumy_user',
        on_delete = models.PROTECT
    )

    def __str__(self):
        return self.goal_name
       

class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length = 150)
    created_by = models.CharField(max_length = 150)
    moved_from = models.CharField(max_length = 150)
    moved_to = models.CharField(max_length = 150)
    time_of_action = models.DateField(default=timezone.now)
    goal = models.ForeignKey(
        ScrumyGoals,
        on_delete = models.PROTECT
    )
    def __str__(self):
        return self.created_by 