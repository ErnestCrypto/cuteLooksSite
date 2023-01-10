from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def loginPage(request):
    context = {}
    return render(request, 'login.html', context)


def signupPage(request):
    context = {}
    return render(request, 'signup.html', context)


def forgetPage(request):
    context = {}
    return render(request, 'forget.html', context)


def indexPage(request):
    context = {
        'index': 'active',
        'about': '',
        'services': '',
        'work': '',
        'blog': '',
        'contact': '',
    }
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        username = firstName + ' ' + lastName
        whatsapp = request.POST.get('whatsapp')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email_client = request.POST.get('email')

        try:

            # email to client
            context = {
                "username": username,
                "email": email_client,
                "phone": whatsapp,
                "index": 'index',
                "message": message
            }
            html_content = render_to_string("email.html", context)
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                subject,
                text_content,
                settings.EMAIL_HOST_USER,
                [email_client]
            )
            email.attach_alternative(html_content, 'text/html')
            email.send()
            # email to cutelooks studios
            content = {
                "username": username,
                "email": email_client,
                "phone": whatsapp,
                "index": 'index',
                "message": message
            }
            html_content2 = render_to_string("receive.html", content)
            text_content2 = strip_tags(html_content2)
            email2 = EmailMultiAlternatives(
                "Client Experience From CuteLooks Website",
                text_content2,
                settings.EMAIL_HOST_USER,
                ["cutelooksgh@gmail.com"]
            )
            email2.attach_alternative(html_content2, 'text/html')
            email2.send()

        except:
            return HttpResponse("Email not successful")

        return redirect('siteAppUrls:confirmPage')

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
    if request.method == 'POST':
        username = request.POST.get('username')
        email_client = request.POST.get('email')
        whatsapp = request.POST.get('whatsapp')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        try:
            # email to client
            context = {
                "username": username,
                "email":  email_client,
                "phone": whatsapp,
                "contact":"contact",
                "message": message,

            }
            html_content = render_to_string("email.html", context)
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                subject,
                text_content,
                settings.EMAIL_HOST_USER,
                [email_client]
            )
            email.attach_alternative(html_content, 'text/html')
            email.send()
            # email to cutelooks studios
            content = {
                "username": username,
                "email":  email_client,
                "phone": whatsapp,
                "contact": "contact",
                "message": message,
            }
            html_content2 = render_to_string("receive.html", content)
            text_content2 = strip_tags(html_content2)
            email2 = EmailMultiAlternatives(
                "Client Enquiries From CuteLooks Website",
                text_content2,
                settings.EMAIL_HOST_USER,
                ["cutelooksgh@gmail.com"]
            )
            email2.attach_alternative(html_content2, 'text/html')
            email2.send()
            
        
            return redirect('siteAppUrls:confirmPage')
        except:
            return HttpResponse("Email not successful")
    else:
        pass

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


def bookingPage(request):
    context = {
        'index': '',
        'about': '',
        'services': 'active',
        'work': '',
        'blog': '',
        'contact': '',
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        booking_type = request.POST.get('booking_type')
        booking_specification = request.POST.get('booking_specification')
        try:
            # email to client
            context = {
                "username": username,
                "email": email,
                "phone": phone,
                "booking_type": booking_type,
                "booking_specification": booking_specification,

            }
            html_content = render_to_string("email.html", context)
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                "Booking Confirmation from CuteLooksSudios",
                text_content,
                settings.EMAIL_HOST_USER,
                [email]
            )
            email.attach_alternative(html_content, 'text/html')
            email.send()
            # email to cutelooks studios
            content = {
                "username": username,
                "email": email,
                "phone": phone,
                "booking_type": booking_type,
                "booking_specification": booking_specification,

            }
            html_content2 = render_to_string("receive.html", content)
            text_content2 = strip_tags(html_content2)
            email2 = EmailMultiAlternatives(
                "Client Bookings From CuteLooks Website",
                text_content2,
                settings.EMAIL_HOST_USER,
                ["cutelooksgh@gmail.com"]
            )
            email2.attach_alternative(html_content2, 'text/html')
            email2.send()

            return redirect('siteAppUrls:confirmPage')
        except:
            return HttpResponse("Email not successful")

    else:
        pass
    return render(request, 'booking.html', context)


def confirmPage(request):
    context = {
        'index': '',
        'about': '',
        'services': 'active',
        'work': '',
        'blog': '',
        'contact': '',
    }
    return render(request, 'confirm.html', context)


def emailPage(request):
    context = {
        "username": 'Ernest',
        "email": 'akotobamfo.eab@gmail.com',
        "phone": '02134122312',
        "booking_type": 'photoshoot',
        "booking_specification": 'full gram',

    }
    return render(request, 'email.html', context)
