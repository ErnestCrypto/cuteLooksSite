from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from twilio.rest import Client

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
        email_from = [email]
        cutelooksWebsite = ["cutelooksgh@gmail.com"]
        cutelooksWebsitemail = "cutelooksgh@gmail.com"

        confirm_message = f"Dear, {firstName} {lastName}, your email has been received successfully. Kindly contact us on our whatsapp number 024 397 1445"
        confrim_subject = "Email Recieved Successfully."
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
        email_from = [email]
        cutelooksWebsite = "cutelooksgh@gmail.com"
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
        try:
            context = {
                "username":username,
                "email":email,
                "phone":phone,
                "booking_type":booking_type,
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
            # kkkkkkkkkkkkk
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
            # sms 
            message_to_broadcast = ("Have you played the incredible TwilioQuest "
                                    "yet? Grab it here: https://www.twilio.com/quest")
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            client.messages.create(to=phone,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)
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
        "email":'akotobamfo.eab@gmail.com',
        "phone": '02134122312',
        "booking_type": 'photoshoot',
        "booking_specification": 'full gram',

    }
    return render(request, 'email.html',context)
