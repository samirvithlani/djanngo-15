from django.shortcuts import render

# Create your views here.
def aboutUs(request):
    return render(request,"aboutus.html")

def aboutYou(request):
    return render(request,"blog/aboutyou.html")    