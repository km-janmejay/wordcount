
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')
def count(request):
    context=request.GET['fulltext']
    wl=context.split()
    res = max(set(wl), key = wl.count)
    freqdic={}
    freq= set(wl)
    for i in freq:
        freqdic[i]=wl.count(i)
    fin=sorted(freqdic.items(),reverse= True)

    return render(request,'count.html',{'fulltext':context , 'length':len(wl),'maxi':res,"allfreq":fin})
def about(request):
    return render(request,'about.html')
