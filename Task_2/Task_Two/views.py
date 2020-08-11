from django.shortcuts import render, HttpResponseRedirect
from .models import User


def index(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')

        user = User(FirstName=fname, LastName=lname, Phone=phone,
                    Email=email, Gender=gender)

        user.save()

        # To clear the form, thus preventing multiple submissions:
        return HttpResponseRedirect('')
    else:
        return render(request, 'StartForm.html')


def view_data(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        match = User.objects.filter(Email=email).first()

        if match:
            return render(request, 'getterPage.html', context={'not_filled': 0,
                                                               'success': 1,
                                                               'match': match})
        else:
            return render(request, 'getterPage.html', context={'not_filled': 0,
                                                               'success': 0})
    else:
        return render(request, 'getterPage.html', context={'not_filled': 1,
                                                           'success': -1})
