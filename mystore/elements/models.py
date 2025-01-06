from django.db import models
from django.contrib import admin
from django.core.exceptions import ValidationError


# Create your models here.
# Tabla -Category
# Columna - atributos (title)
class Category(models.Model):
    title = models.CharField(max_length= 255)
    slug = models.SlugField(max_length= 255)
    
    def __str__(self) -> str:
        return self.title
    
class Type(models.Model):
    title = models.CharField(max_length= 255)
    slug = models.SlugField(max_length= 255)
    
    def __str__(self) -> str:
        return self.title
    
class Element(models.Model):
    title = models.CharField(max_length= 255)
    slug = models.SlugField(max_length= 255, unique=True, blank=True) # Slug es blanco
    description = models.TextField()
    price = models.DecimalField(max_digits= 10, decimal_places= 2, default= 6.10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True)
    
    # Agregamos la funcion cheap que sera un nuevo campo
    # el True hace el comportamiento de palomita y tache si le pones FALSE regresa el true y false
    @admin.display(boolean=True)
    def cheap(self):
        return 0 <= self.price < 9.9
    
    def __str__(self) -> str:
        return self.title
    
    def clean(self):
        if self.price < 0:
            raise ValidationError("Precio no puede ser < 0 ")
        
    
