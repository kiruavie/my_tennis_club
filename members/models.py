from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phones = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    # Change the String Representation Function : __str__
    # def __str__(self):
    #     return f"{self.firstname} {self.lastname}"
    


     
