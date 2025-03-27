from django.shortcuts import render

def habits(request):
    return render(request, 'habits\\habits.html')

def statistics(request):
    return render(request, 'habits\\statistics.html')