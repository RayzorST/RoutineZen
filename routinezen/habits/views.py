from django.shortcuts import render

def habits(request):
    addTracker = False
    if 'add' in request.POST:
        addTracker = True
    if 'confirm' in request.POST:
        pass
    if 'close' in request.POST:
       pass
    return render(request, 'habits\\habits.html', {"addTracker" : addTracker})

def statistics(request):
    return render(request, 'habits\\statistics.html')