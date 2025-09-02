from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import  redirect

'''
===============================================================================================================
                    Homepage method
===============================================================================================================
'''
from django.shortcuts import render
from .models import App

def home_view(request):
    apps = App.objects.filter(is_active=True)

    return render(request, "index.html", {"apps": apps})


'''
===============================================================================================================
                 Download file method
===============================================================================================================
'''


from django.shortcuts import get_object_or_404
from django.http import FileResponse, Http404
from .models import App
from django.http import JsonResponse


def download_app_file(request, app_id):
    app = get_object_or_404(App, id=app_id, is_active=True, is_deleted=False)

    if not app.download_file:
        raise Http404("File not found.")
   
    response = FileResponse(
        app.download_file.open("rb"),
        # file ko binary read mode me open kar raha hai.
        as_attachment=True,
        # iska matlab file download hogi, browser me open nahi hogi (jaise PDF ko open karne ki jagah download prompt aayega).
        filename=app.download_file.name.split("/")[-1] 
        # file ka naam set karta hai jo download hone par dikhai dega.
    )
    print(f'{response=}')
    return response


'''
===============================================================================================================
                 Download count method
===============================================================================================================
'''


def update_download_count(request, app_id):
    if request.method == "POST":
        app = get_object_or_404(App, id=app_id, is_active=True, is_deleted=False)
        app.download_count += 1
        app.save(update_fields=["download_count"])
        # Ye line database me update save karti hai.
        return JsonResponse({"success": True, "count": app.download_count})
    return JsonResponse({"success": False}, status=400)
