import json

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import UserDetails, CourseDetails


# Create your views here.
def login(request):
    return render(request, "login.html")


def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        user = UserDetails.objects.filter(email_id=email, password=password).first()
        if user is not None:
            request.session['my_pass'] = user.password
            request.session['user_name'] = user.user_name
            login(request)
            # Redirect to a success page or dashboard
            # return redirect('dashboard')
            return render(request, "index.html")
        else:
            pass
            # messages.error(request, 'Invalid email or password.')

    return render(request, "login.html")


def short_course_view(request):
    return render(request, "short-course-view.html")


def short_course_create(request):
    return render(request, "short-course-create.html")


def add_new_course(request):
    data = request.POST.dict()
    if request.method == "POST":
        subtitle = request.POST["subtitle"]
        image_file = request.FILES["image"]
        if image_file:
            file_name = f'{data.get("name")}_{subtitle}_{image_file.name}'
            file_content = image_file.read()
            path = default_storage.save(
                "images/" + file_name, ContentFile(file_content)
            )

            dict = {
                "name": data.get("name"),
                "subtitle": data.get("subtitle"),
                "amount": data.get("amt"),
                "amount_in_words": data.get("amt2"),
                "description": data.get("description"),
                "image": path,
            }
            dict_save = CourseDetails.objects.create(**dict)
            dict_save.save()

            return HttpResponse(
                json.dumps({"msg": "Image saved successfully", "status": "success"}),
                content_type="application/json",
            )
        else:
            return HttpResponse(
                json.dumps({"msg": "No image provided", "status": "faild"}),
                content_type="application/json",
            )

def profile(request):
    return render(request, 'profile.html')

@csrf_exempt
def password_change(request):
    status = {}
    req_data = request.POST.dict()
    if req_data.get('currentPassword') == request.session['my_pass']:
        if req_data.get('newPassword') == req_data.get('confPassword'):
            breakpoint()
            user = UserDetails.objects.filter(user_name=request.session['user_name'])
            user.old_password = user.password
            user.password = req_data.get('newPassword')
            user.save()
            status = {'msg':'password changed', 'sts':True}
        else:
            status = {'msg':'password miss matching', 'sts':False}
        
    else:
        status = {'msg':'incorrect password','sts':False}

    return HttpResponse(json.dumps(status), content_type="application/json")