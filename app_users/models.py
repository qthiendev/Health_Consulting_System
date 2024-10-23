from django.db import models
from django.contrib.auth.models import User

class MedicalHistory(models.Model):
    profile = models.ForeignKey('Profile', related_name='medical_histories', on_delete=models.CASCADE)
    item = models.CharField(max_length=255)

    def __str__(self):
        return self.item

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.CharField(null=True, blank=True, max_length=10)
    address = models.CharField(null=True, max_length=255)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)
    exercise_level = models.CharField(
        null=True,
        max_length=50,
        choices=[
            ('sedentary', 'Ít vận động'),
            ('lightly_active', 'Vận động nhẹ'),
            ('moderately_active', 'Vận động vừa phải'),
            ('very_active', 'Vận động nhiều'),
            ('super_active', 'Vận động cực nhiều'),
        ],
        default='sedentary'
    )

    def __str__(self):
        return self.user.username