from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail

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
        whatsapp = request.POST.get('whatsapp')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        message_send = f"{message}. My whatsapp number is {whatsapp}"
        email = request.POST.get('email')
        email_from =[email]
        cutelooksWebsite = ["cutelooksgh@gmail.com"]
        cutelooksWebsitemail = "cutelooksgh@gmail.com"

        confirm_message = f"Dear, {firstName} {lastName}, your email has been received successfully. Kindly contact us on our whatsapp number 024 397 1445"
        confrim_subject ="Email Recieved Successfully."
        send_mail(subject, message_send, email, cutelooksWebsite)
        send_mail(confrim_subject, confirm_message,
                  cutelooksWebsitemail, email_from)
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
        email = request.POST.get('email')
        whatsapp = request.POST.get('whatsapp')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        f_message = f"{message}. My whatsapp number is {whatsapp}"
        recipient_list = ['cutelooksgh@gmail.com']
        email_from =[email]
        cutelooksWebsite ="cutelooksgh@gmail.com"
        confirm_subject = "Email Recieved Successfully."
        confirm_message = f"Dear, {username}.Your email has been received successfully. Kindly get in touch with us through our whatsapp number 024 397 1445 for better assistance. Thank you"
        send_mail(subject, f_message, email, recipient_list)
        send_mail(confirm_subject, confirm_message,
                  cutelooksWebsite, email_from)
        return redirect('siteAppUrls:confirmPage')
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
        subject = 'Client Bookings'
        cleint_subject = 'Bookings Confirmed'
        message = f"Hello, please my name is {username} and I would like to book the {booking_type}, {booking_specification} makeup package. I can be contacted on {phone}"
        client_message = f"Hi,{username}.Your booking has been received successfully. You will be contacted on {phone} shortly. "
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['cutelooksgh@gmail.com']
        client_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        send_mail(cleint_subject, client_message, email_from, client_list)
        return redirect('siteAppUrls:confirmPage')
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
