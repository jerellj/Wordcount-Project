
from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html',{'Hi':'This is me'})

def jerell(request):
    return HttpResponse("Ja mijn naam is Jerell")

def count(request):
    text = request.GET['full']
    all = text.split()

    worddic = {}

    for word in all:
        if word in worddic:
            worddic[word] += 1
        else:
            worddic[word] = 1

    wordSorted = sorted(worddic.items(),key=operator.itemgetter(1), reverse=True)

    return render(request,"count.html",{'text':text,'count':len(all),'worddic':wordSorted})

def about(request):
    return render(request, 'About.html')
