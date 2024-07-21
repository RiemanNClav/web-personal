from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    link = models.URLField(verbose_name="Direccion Web", null=True, blank=True)

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blog"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title
    