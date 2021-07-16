from django.db import models

# Create your models here.


class MyModel(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employer(MyModel):
    class Meta:
        db_table = 'hr_employer'
    name = models.CharField(max_length=255, unique=True, null=False)

    def __str__(self):
        return f'{type(self)} {self.id}'