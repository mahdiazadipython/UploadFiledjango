from django.db import models



class Base(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.SlugField(max_length=100)

    def __str__(self):
        return self.title



class TutorailDjango(models.Model):
    name  = models.ForeignKey(Base,on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    slug   = models.SlugField(max_length=100)
    cover  =models.FileField(upload_to ="mahdi/")
    available = models.BooleanField(default = True)

    def __str__(self):
        return self.title
