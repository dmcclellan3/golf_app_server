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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.course.name} on {self.date}"

class Hole(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    hole_number = models.IntegerField()
    par = models.IntegerField()

    def __str__(self):
        return f"Hole {self.hole_number} (Par {self.par}) - {self.course.name}"

class Score(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    hole = models.ForeignKey(Hole, on_delete=models.CASCADE)
    strokes = models.IntegerField()

    def __str__(self):
        return f"{self.round} - Hole {self.hole.hole_number}: {self.strokes} strokes"
