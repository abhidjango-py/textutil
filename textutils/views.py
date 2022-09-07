from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render (request,'index.html')

def analyze(request):
    val=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspace=request.POST.get('extraspace','off')
    charcount=request.POST.get('charcount','off')


    if removepunc=="on":
        analyzed=''
        punc='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in val:
            if char not in punc:
                analyzed=analyzed+char
        params={'analyzedtext':analyzed}
        val=analyzed

    if fullcaps=='on':
        analyzed=''
        for char in val:
            analyzed=analyzed+char.upper()
        params={'analyzedtext':analyzed}
        val=analyzed

    if newlineremove=='on':
        analyzed=''
        for char in val:
            if char!=("\n") and char!=("\r"):
                analyzed=analyzed+char
        params={'analyzedtext':analyzed}
        val=analyzed

    if extraspace=='on':
        analyzed=''
        for index,char in enumerate(val):
            if not(val[index]==" " and val[index+1]==" "):
                analyzed=analyzed+char
        params={'analyzedtext':analyzed}
        val=analyzed

    if charcount=='on':
        analyzed=''
        analyzed=len(val)
        params={'analyzedtext':analyzed}

    if removepunc!='on' and fullcaps!='on' and newlineremove!='on' and extraspace!='on' and charcount!='on':
        analyzed="Please turn on some analyzer"
        params={'analyzedtext':analyzed}

    return render(request,'analyzed.html',params)