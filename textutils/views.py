# ihave created this website -nisha

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params={'Name':'Nisha','Place':'Patna'}
    return render(request,'index.html',params)

def analyze(request):
    djtext=(request.POST.get('text','default'))
    removepunc=request.POST.get('removepunc','off')
    extraspaceremov=request.POST.get('extraspaceremov','off')
    fullcap = request.POST.get('fullcap', 'off')
    countWords=request.POST.get('countWords', 'off')
#remove punchuation
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
        #Handling the extra spaces present in texxt
    if(extraspaceremov=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed
    #convert it into upper case letter
    if(fullcap=="on"):
        analyzed = ""
        for char in djtext:

                analyzed = analyzed + char.upper()

        params = {'purpose': 'Convert to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed

#counting the word of paragraph
    if (countWords=="on"):
        count =0
        for index, char in enumerate(djtext):
            if (djtext[index] == " " and djtext[index + 1] == " "):
                count+=1

        params = {'purpose': 'Count words', 'analyzed_text':count}
        djtext=analyzed
#Nothing is selected show the error page
    if (removepunc != "on" and extraspaceremov != "on" and fullcap!= "on"):
        return render(request, 'error.html')
        #return HttpResponse("please select any operation and try again")
    return render(request, 'analyze.html', params)







