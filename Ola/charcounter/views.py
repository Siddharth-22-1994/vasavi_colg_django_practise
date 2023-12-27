from django.shortcuts import render

# Create your views here.

def charcounterview(request):
    if request.method=='POST':
        text=request.POST['clienttext']
        total_length = len(text)
        words = len(text.split(" "))
        
        context={
            "text":text,
            "char_length":total_length,
            "words":words
        }
        return render(request, 'charcount.html', context)
    return render(request, 'charcount.html')