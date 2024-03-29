# KRISH SONI
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'index.html')

@csrf_protect
def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    wordcount = request.POST.get('wordcount', 'off')
    numberremover = request.POST.get('numberremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (numberremover == "on"):
        analyzed = ""
        numbers = '0,1,2,3,4,5,6,7,8,9'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Numbers', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount == "on"):
        analyzed = len(djtext)

        params = {'purpose': 'Character Count ', 'analyzed_text': analyzed}
        djtext = analyzed

    if (wordcount =="on"):

       analyzed = len(djtext.split())
       print(str(analyzed))
       djtext=analyzed

       params = {'purpose': 'Word Count', 'analyzed_text': analyzed}
       djtext = analyzed



# last parameters


    if(removepunc != "on" and newlineremover!="on" and numberremover!="on" and extraspaceremover!="on" and fullcaps!="on" and charcount!="on" and wordcount!="on"):
        return render(request,'error404.html')

    return render(request, 'analyze.html', params)
