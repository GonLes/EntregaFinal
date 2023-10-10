from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Avatar

@receiver(post_save, sender=User)
def create_user_avatar(sender, instance, created, **kwargs):
    if created:
        avatar = Avatar.objects.create(user=instance, imagen='avatares/profile_default.jpg')

@receiver(post_save, sender=User)
def save_user_avatar(sender, instance, **kwargs):
    instance.avatar.save()
