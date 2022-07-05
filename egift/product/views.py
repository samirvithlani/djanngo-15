

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import *

# Create your views here.
def index(request):
    #select * from product
    #queryset
    product_list = Product.objects.all().values_list()
    product_list1 = Product.objects.filter(product_availablity=False).values_list()
    product_list2 = Product.objects.filter(product_price__lt= 500000).values_list()
    product_list3 = Product.objects.filter(product_name__startswith='i').values_list()
    print(product_list)    
    print(product_list1) 
    print(product_list2)  
    print(product_list3)  
    return HttpResponse('This is index')

def index1(request):
    students = Student.objects.all().values_list()
    #do natural join using django orm
    students1 = Student.objects.all().values('course__course_name','sname','sage')
    print(students)
    print(students1)
    
    return HttpResponse("ok")

class DemoCreateView(CreateView):
    model  =Demo
    fields = ['username','profile_pic']
    template_name = "demo.html"
    success_url = "/"
    