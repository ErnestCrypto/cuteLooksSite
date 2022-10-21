from django.shortcuts import render


def indexPage(request):
    context = {}
    return render(request, 'index.html', context)
