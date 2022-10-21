from django.shortcuts import render


def indexPage(request):
    context = {}
    return render(request, 'index.html', context)


def aboutPage(request):
    context = {}
    return render(request, 'about.html', context)


def blog_singlePage(request):
    context = {}
    return render(request, 'blog-single.html', context)


def blogPage(request):
    context = {}
    return render(request, 'blog.html', context)


def contactPage(request):
    context = {}
    return render(request, 'contact.html', context)


def servicesPage(request):
    context = {}
    return render(request, 'services.html', context)


def workPage(request):
    context = {}
    return render(request, 'work.html', context)
