from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    # def __str__(self) -> str:
    #     return super().__str__()

    # this return Drink model as string ( Ex: Grape soda Very grapy )
    def __str__(self):
        return self.name + ' ' + self.description

    # if commenet above would return as a Object (Ex: Drink object (1) )