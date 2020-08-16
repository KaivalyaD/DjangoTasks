from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import User as Extended_User
from django.contrib.auth.models import User

logged_out_successfully = 'False'


def user_signup_view(request):
    global logged_out_successfully
    logged_out_successfully = 'False'  # Setting the is_last_action_logout to false
    # I Spent a lot of time figuring out how to display the logout
    # message in the 'proper' way. Please guide me regarding this...

    if request.method == 'POST':

        data = request.POST
        epass = data.get('pass')  # Entered Password
        cpass = data.get('cpass')  # Confirm Password

        if epass == cpass:
            username = data.get('user')
            email = data.get('email')
            fname = data.get('fname')
            lname = data.get('lname')
            phone = data.get('phone')

            try:
                # New Built in user
                new_user = User.objects.create_user(username, email, epass, first_name=fname, last_name=lname)
                new_user.save()
                # Extended User
                user_with_phone = Extended_User(phone_no=phone, user=new_user)
                user_with_phone.save()

                auth_user = authenticate(request, username=username, password=epass)

                if auth_user is not None:
                    login(request, auth_user)
                    return render(request, 'success.html', context={'user': auth_user})

            except IntegrityError:
                return render(request, 'signup.html', context={'error': 'user_exists'})

        else:
            return render(request, 'signup.html', context={'error': 'unmatched_pass'})

    return render(request, 'signup.html')


def user_login_view(request):
    global logged_out_successfully
    if request.method == 'POST':
        username = request.POST.get('user')
        pass_e = request.POST.get('auth_pass')

        user = authenticate(request, username=username, password=pass_e)

        if user is not None:
            return render(request, 'success.html', context={'user': user})
        else:
            logged_out_successfully = 'False'  # Resetting the is_last_action_logout state to false
            return render(request, 'login.html', context={'error': 'cred_inv'})

    return render(request, 'login.html', context={'log_state': logged_out_successfully})


def user_logout_view(request):
    global logged_out_successfully
    logout(request)
    logged_out_successfully = 'True'  # Setting the is_last_action_logout state to true
    return redirect('login')
