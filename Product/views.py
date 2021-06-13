from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"position-sekli.html")
def deneme(request):
    return render(request,"deneme.html")