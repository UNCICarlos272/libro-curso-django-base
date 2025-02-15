from django.db import models
from elements.models import Element

# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now= True)
    elemet = models.ForeignKey(Element, on_delete=models.CASCADE, null= True)
    
    def __str__(self) -> str:
        return 'Comment #{}'.format(self.id)
    
#class Test(models.Model):
#    text = models.TextField()