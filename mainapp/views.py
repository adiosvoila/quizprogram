

# Create your views here.

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'mainapp/index.html')

def quizpage(request):
    return render(request,'mainapp/quizpage.html')
