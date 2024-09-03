from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from app.models import PersonalDetails, MoreDetails, SocialLinks, NewMessages


def BaseLoading(request):
    return render(request, 'base.html')


def HomeLoading(request):
    personalDetails = PersonalDetails.objects.get(first_name="Saeedh")
    person_id = personalDetails.id
    moreDetails = MoreDetails.objects.get(person_id=person_id)
    socialLinks = SocialLinks.objects.get(person_id=person_id)
    context = {"personalDetails":personalDetails, 'moreDetails':moreDetails, 'socialLinks':socialLinks}
    return render(request, 'home.html', context)


def AboutLoading(request):
    personalDetails = PersonalDetails.objects.get(first_name="Saeedh")
    context = {"personalDetails":personalDetails}
    return render(request, 'about.html', context)


def ResumeLoading(request):
    personalDetails = PersonalDetails.objects.get(first_name="Saeedh")
    context = {"personalDetails":personalDetails}
    return render(request, 'resume.html', context)


def CerticicatesLoading(request):
    personalDetails = PersonalDetails.objects.get(first_name="Saeedh")
    context = {"personalDetails":personalDetails}
    return render(request, 'certificates.html', context)


def ContactLoading(request):
    personalDetails = PersonalDetails.objects.get(first_name="Saeedh")
    person_id = personalDetails.id
    moreDetails = MoreDetails.objects.get(person_id=person_id)
    context = {"personalDetails":personalDetails, 'moreDetails':moreDetails}
    return render(request, 'contact.html', context)


def DwonloadResume(request):
    personalDetails = get_object_or_404(PersonalDetails, first_name="Saeedh")
    if personalDetails.resume:
        response = HttpResponse(personalDetails.resume, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{personalDetails.first_name}_{personalDetails.second_name}.pdf"'
        return response
    else:
        return HttpResponse("No resume available.", status=404)


def NewMessageSaving(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        message = request.POST['message']

        message_info = NewMessages(name=name, email_id=email, mobile_no=mobile, message=message)
        message_info.save()

        send_mail(
                subject=f"Message from {name}",
                message=message,
                from_email=email,
                recipient_list=['saeedhmohd244@gmail.com'],
        )

        messages.success(request,"Your Resopnse Is Recived")
        return redirect('HomeLoading')
    else:
        messages.error(request,"error")
        return redirect('HomeLoading')