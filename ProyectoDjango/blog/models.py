from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    autor = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,null=True
    )
    cuerpo = models.TextField()
    creado=models.DateField(auto_now_add=True,editable=False)
    modificado=models.DateField(auto_now=True)
    def __str__(self):
        return f'{self.titulo}-{self.autor}-{self.creado}'

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})



class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
        
    def __str__(self):
        return f"{self.user} - {self.imagen}"

