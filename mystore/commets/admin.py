from django.contrib import admin

from .models import Comment
# Register your models here.

@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    #list_display = ('id', 'text') # nos muestra el id y el texto
    #search_fields = ('id', 'text') # los campos de busqueda 
    #date_hierarchy = 'date_posted' # campo para la fecha - busqueda por fecha
    #ordering = ('date_posted',) # ordenar segun ciertos campos 
    #list_filter = ('id', 'date_posted') # filtrado desde una columna en la derecha del display 
    #list_editable = ('text', ) # te permite editar este campo desde el display
    #fields = ('text',) # Los campos que queremos administrar en este caso solo texto y elementos no 
    exclude = ('elemet',) # es lo contrario a fields - todos los campos menos element (negativa de fields)
    save_as = True #- nos aparece la opcion de guardar como nuevo (clona el registro)
    #save_on_top = True # las opciones de guardado aparecen arriba.
    
    #class Media:
    #    css = {
    #        "all" : ["my_style.css"]
    #    }
    
    # Nos permiten realizar una operacion entes de eliminar o guardar algun valor 
    def delete_queryset(self, request, queryset): # es cuando se eliminan en grupo
        print('delete')
        super().delete_queryset(request, queryset) # se puede ejecutar el codigo antes de realizar la opracion si se coloca antes de esta linea de codigo
    
    def delete_model(self, request, obj): # de forma individual
        super().delete_model(request, obj)
    
    def save_model(self, request, obj, form, change):
        print("save before")
        super().save_model(request, obj, form, change)
        print('afeter')

#admin.site.register(Comment, CommentAdmin)


