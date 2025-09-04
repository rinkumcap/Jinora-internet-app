from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from app.models import *
from .forms import AppForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import AdminUser
from django.views.decorators.csrf import csrf_exempt
'''
===============================================================================================================
                        Admin Login method
===============================================================================================================
'''
@csrf_exempt
def admin_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('Email', '').strip()
        print(f'{email=}')
        password = request.POST.get('password', '').strip()
        print(f'{password=}')
        admindt = AdminUser.objects.filter(admin_email=email).first()
        if admindt:  # user mila
            if password == str(admindt.admin_password): 
                request.session['admin_id'] = admindt.admin_id 
                return redirect('dashboard_view') 
            else: messages.error(request, 'Wrong password.') 
        
        else:
            messages.error(request, "Admin not found.")

    return render(request, 'admin_login.html')

'''
===============================================================================================================
                        Dashboard method
===============================================================================================================
'''


def dashboard_view(request):
    if 'admin_id' not in request.session:
        return redirect('admin_login')
    android_count = App.objects.filter(platform = "android" ,is_deleted=False).count()
    ios_count = App.objects.filter(platform = "ios",is_deleted=False).count()
    print(f"{android_count=},{ios_count=}")
    return render(request,'dashboard.html',{"android_count":android_count,"ios_count":ios_count})



'''
===============================================================================================================
                        Admin Logout method
===============================================================================================================
'''
from django.shortcuts import redirect
from django.contrib import messages

def admin_logout_view(request):
 
    if 'admin_id' in request.session:
        del request.session['admin_id']
    
    # Optional: puri session clear karne ke liye
    # request.session.flush()

    messages.success(request, "Logged out successfully!")
    return redirect('admin_login')  


'''
===============================================================================================================
                       App method
===============================================================================================================
'''


def app_list(request):
    if 'admin_id' not in request.session:
        return redirect('admin_login')
    app_list = App.objects.all()
    return render(request, "app_list.html", {"app_list": app_list})

@csrf_exempt
def app_add(request):

    if 'admin_id' not in request.session:
        return redirect('admin_login')
    if request.method == "POST":
        form = AppForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "app added successfully!")
            return redirect("app_list")
    else:
        form = AppForm()
    return render(request, "app_form.html", {"form": form, "title": "Add App"})


def app_edit(request, app_id):
    if 'admin_id' not in request.session:
        return redirect('admin_login')
    app = get_object_or_404(App, pk=app_id)
    if request.method == "POST":
        form = AppForm(request.POST, request.FILES, instance=app)
        print(f'{form=}')
        if form.is_valid():
        
            form.save()
            messages.success(request, "App updated successfully!")
            return redirect("app_list")
    else:
        form = AppForm(instance=app)
    return render(request, "app_form.html", {"form": form, "title": "Edit App"})





def app_delete(request, app_id):
    if 'admin_id' not in request.session:
        return redirect('admin_login')

    app = get_object_or_404(App, pk=app_id)
    app.delete()
    # app.is_deleted = True
    # app.save()
    messages.success(request, "App deleted successfully!")
    return redirect("app_list")



'''
===============================================================================================================
                    Tota   App method
===============================================================================================================
'''

