from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Challenge(models.Model):

    CHALLENGE_FIELD = (
        ('Web', 'Web'),
        ('Pwnable', 'Pwnable'),
    )

    title = models.CharField(max_length=100)
    body = models.TextField()
    flag = models.TextField()
    field = models.CharField(max_length=10, choices=CHALLENGE_FIELD)
    score = models.IntegerField(unique= True)
    challengefile = models.FileField(blank = True)

    def __str__(self):
        return self.title

    
class Writeup(models.Model):
    challenge = models.ForeignKey('hackusapp.Challenge', on_delete=models.CASCADE, related_name='writeup')
    author = models.CharField(max_length = 18)
    date=models.DateTimeField(default = timezone.now)
    body=models.TextField(null = True)
    onoff=models.BooleanField("onoff", default=False)

    def __str__(self):
        return str(self.challenge) + str(self.author)

class Success(models.Model):
    challenge = models.ForeignKey('hackusapp.Challenge', on_delete=models.CASCADE, related_name='challenge_id')
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    points= models.ForeignKey('hackusapp.Challenge', to_field='score', on_delete=models.CASCADE, related_name = 'points', null=True)

    def __str__(self):
        return str(self.challenge) + str(self.user) + str(self.points)