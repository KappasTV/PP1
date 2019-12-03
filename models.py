from django.db import models

class Family(models.Model):
    family_name = models.CharField('Family name', max_length = 200)
    father_name = models.CharField('Father`s name', max_length = 50)
    mother_name = models.CharField('Mother`s name', max_length = 50)
    child_name = models.CharField('Child`s name', max_length = 50)
    family_budget = models.IntegerField()
    father_budget = models.IntegerField()
    mother_budget = models.IntegerField()
    child_budget = models.IntegerField()
    
    def __str__(self):
        return self.family_name


class Perevod(models.Model):
    perevod = models.ForeignKey(Family, on_delete = models.CASCADE)
    user_name = models.CharField('Name of member who done operation', max_length = 50)
    user_perevod = models.IntegerField()
