from django.db import models

# Create your models here.
class Evenement(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "evenements"