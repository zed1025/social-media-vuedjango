from django.db import models
from django.contrib.auth.models import User


class OinkerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)


User.oinkerprofile = property(lambda u: OinkerProfile.objects.get_or_create(user=u)[0])
