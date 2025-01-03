from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404# get_object_or_404 # renderizar un templete
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from .models import Comment

# importamos el formulario
from .forms import CommentForm

# Create your views here.
#def home_page_view(request):
#    return HttpResponse("Hola Mundo")

#def home_page_view_2(request):
#    return HttpResponse("Mi segunda vista")
"""
def add(request):
    #return render(request, 'Carlos_Pena_Portafolio-main\index.html', {'data': 'Primer Valor', 'data2': 'este es el segundo valor'})
    print(request.method)
    if(request.method == 'GET'):
        pass
    if(request.method == 'POST'):
        #SAVE
        if request.POST.get('text') != '':
            comment = Comment()
            comment.text = request.POST.get('text')
            comment.save()
        else: 
            print("Campo vacio")
    
    return render(request, 'add.html')
"""


def add(request):
    if(request.method == 'POST'):
        form = CommentForm(request.POST)
        comment = form.save()
        return redirect('commets:index')
    else:
        form = CommentForm()
    return render(request, 'comments/add.html', {'form':form})


def index(request):
    
    #comments = Comment.objects.all()
    comments = get_list_or_404(Comment, pk__gt = 12) # Select * From comments Where id > 12
    paginator = Paginator(comments, 2)
    
    page_number = request.GET.get('page')
    comments_page = paginator.get_page(page_number)
    
    return render(request, 'comments/index.html', {'comments' : comments_page})

def update(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    #Aqui funciona lo de las secciones por lo tanto se ocupa try
    #try:
    #    comment = Comment.objects.get(pk = pk)
    #except Comment.DoesNotExist:
    #    raise Http404
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('commets:index')
    else:
        form = CommentForm(instance=comment)
        
    return render(request, 'comments/add.html', {'form':form})

def delete(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    #comment = Comment.objects.get(pk = pk)
    
    if request.method == 'POST':
        comment.delete()
        return redirect('commets:index')