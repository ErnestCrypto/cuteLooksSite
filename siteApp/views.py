from django.shortcuts import render


def loginPage(request):
    context = {}
    return render(request, 'login.html', context)


def indexPage(request):
    context = {
        'index': 'active',
        'about': '',
        'services': '',
        'work': '',
        'blog': '',
        'contact': '',
    }
    return render(request, 'index.html', context)


def aboutPage(request):
    context = {
        'index': '',
        'about': 'active',
        'services': '',
        'work': '',
        'blog': '',
        'contact': '',
    }
    return render(request, 'about.html', context)


def blog_singlePage(request):
    context = {
        'index': 'active',
        'about': '',
        'services': '',
        'work': '',
        'blog': '',
        'contact': '',
    }
    return render(request, 'blog-single.html', context)


def blogPage(request):
    context = {
        'index': '',
        'about': '',
        'services': '',
        'work': '',
        'blog': 'active',
        'contact': '',
    }
    return render(request, 'blog.html', context)


def contactPage(request):
    context = {
        'index': '',
        'about': '',
        'services': '',
        'work': '',
        'blog': '',
        'contact': 'active',
    }
    return render(request, 'contact.html', context)


def servicesPage(request):
    context = {
        'index': '',
        'about': '',
        'services': 'active',
        'work': '',
        'blog': '',
        'contact': '',
    }
    return render(request, 'services.html', context)


def workPage(request):
    context = {
        'index': '',
        'about': '',
        'services': '',
        'work': 'active',
        'blog': '',
        'contact': '',
    }
    return render(request, 'work.html', context)
