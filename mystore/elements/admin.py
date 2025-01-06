from django.contrib import admin
from.models import Category, Type, Element
from django import forms
from django.utils.text import slugify

# Register your models here.
# Editar formulario 

#class ElementForm(forms.ModelForm):
#    class Meta:
#        model = Element
#        exclude = ["title"]

#class ElementInline(admin.TabularInline): # apaerece en filas
#    model = Element
#class ElementInline(admin.StackedInline): # aparece en formulario 
#    model = Element

@admin.register(Category, Type)
class CategoryTypeAdmin(admin.ModelAdmin):
    list_display =('id','title')
    # En la clase relacional
    #inlines = [
    #    ElementInline
    #]

#Nos permite crear el campo con el id y el titulo
@admin.display(description="ID - title en mayusculas")
def upper_title(obj):
    return f"{ obj.id}  {obj.title}".upper()

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):        
    list_display =('id','title','category','type',upper_title, "cheap")
    #fields = (('title','slug'),'description','price',('category','type'))
    fieldsets = [
        (
            'Regular options',
            {
                "fields":(('title','slug'),'description',('category','type'))
            }
        ),
        (
            'Advanced options',
            {
                "fields":('price',),
                "classes": ['collapse'] # esta opcion nos permite colapsar estos campos y el usuario los muestra
            }
        )
    ]
    
    #form = ElementForm
    def save_model(self, request, obj, form, change):
        if not(change) and obj.slug == '':
            obj.slug = slugify(obj.title)
        
        if obj.slug == '':
            obj.slug = slugify(obj.title) #quita espacios por - y quita caracteres especiales (slugufy) 
        super().save_model(request, obj, form, change)
