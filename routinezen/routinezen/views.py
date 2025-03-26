from django.shortcuts import render, redirect

def main(request):
    if 'start' in request.POST:
        return redirect("/account")
    return render(request, 'main\\hello.html')