#from .views import add #home_page_view, home_page_view_2
from django.urls import path
from . import views

app_name = 'commets'

urlpatterns = [
    #path('home/',home_page_view, name= 'home'),
    #path('home2/',home_page_view_2, name= 'home2')
    path('add/', views.add, name= 'add'),
    path('', views.index, name= 'index'),
    path('/update/<int:pk>', views.update, name= 'update'),
    path('/delete/<int:pk>', views.delete, name= 'delete')
]
#action = "add.html"