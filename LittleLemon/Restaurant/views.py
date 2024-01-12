from django.shortcuts import render

def sampleView(request):
    return render(request, 'index.html', {}) 
