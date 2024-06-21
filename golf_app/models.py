from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Course(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Round(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rounds')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='rounds')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.id} - {self.user.username} - {self.course.name} on {self.date}"

class Score(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='scores')
    hole = models.ForeignKey('Hole', on_delete=models.CASCADE, related_name='holes', null=True)
    strokes = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.strokes} strokes'
        


class Hole(models.Model):
    # round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='holes', null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='holes')
    score = models.ForeignKey(Score, on_delete=models.CASCADE, related_name='scores', null=True, blank=True)
    hole_number = models.IntegerField()
    par = models.IntegerField()

    def __str__(self):
        return f"ID: {self.id} - Hole {self.hole_number} (Par {self.par}) - {self.course.name}"