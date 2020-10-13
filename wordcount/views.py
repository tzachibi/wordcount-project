from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html',{'a':'this value s from a directory'})

def count(request):
    text1 = request.GET['fulltext']
    print(text1)
    list=text1.split()

    hWords = {}
    for word in list:
        if word in hWords:
            hWords[word] += 1
        else:
            hWords[word] = 1
        
    list = sorted(hWords.items(),key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html', {'fulltext':text1,'num':len(list), 'hWords':list})

def about(request):
    return render(request,'about.html')
