"""
loginapp/views.py
"""

from django.shortcuts import render, HttpResponse

# Create your views here.
def my_login_page(request):
    return render(request, 'userlogin.html', {})

def my_register_page(request):
    return render(request, 'userregister.html', {})

def my_addnewuser_page(request):
    """
    Form data will be captured by framwork and it will keep im
    POST request: request.POST dictionary
    PUT request: request.PUT dictionary
    """

    from .models import UserModel

    if request.method == "POST":
        entered_username = request.POST.get('uname')
        entered_password_1 = request.POST.get('pw1')
        entered_password_2 = request.POST.get('pw2')
        entered_email = request.POST.get('email')
        entered_contact = request.POST.get('contact')
        if entered_password_1 != entered_password_2:
            return redirect('/login/register/?error=Both%20Passwords%20should%20match')

        users_count = UserModel.objects.filter(username=entered_username).count()
        if users_count > 0:
            return redirect('/login/register/?error=Account%20already%20exists')
        else:
            new_user = UserModel()
            new_user.username = entered_username
            new_user.password =entered_password_1
            new_user.email = entered_email
            new_user.contact = entered_contact
            new_user.save()
            request.session["username"] = entered_username
            return redirect('/login/register/?success=1') #success register
    else:
        return redirect('/login/register/?error=1')

from .models import UserModel, AdminModel
from django.shortcuts import redirect

def my_validatelogin_page(request):
    if request.method == "POST":
        entered_username = request.POST.get('uname')
        entered_password_1 = request.POST.get('pw')

        users_count = UserModel.objects.filter(username=entered_username, password=entered_password_1).count()

        if users_count > 0:
            request.session["username"] = entered_username
            return redirect('/login/?success=1')
        else:
            return redirect('/login/?error=1')  # Redirect to the login page with an error parameter
    else:
        return HttpResponse("Method Not Supported")


def my_admin_login_page(request):
    return render(request, 'adminlogin.html', {})

def my_admin_validatelogin_page(request):
    if request.method == "POST":
        entered_username = request.POST.get('uname')
        entered_password_1 = request.POST.get('pw')

        users_count = AdminModel.objects.filter(username=entered_username, password=entered_password_1).count()

        if users_count > 0:
            request.session["adminusername"] = entered_username
            return redirect('/login/admin/?success=1')
        else:
            return redirect('/login/admin/?error=1')  # Redirect to the login page with an error parameter
    else:
        return HttpResponse("Method Not Supported")

