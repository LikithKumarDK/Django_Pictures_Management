# frontend/views.py
from django.shortcuts import render
from django.http import JsonResponse
# from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from .models import Image
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime


def index(request):
    return render(request, 'base.html')


@csrf_exempt
def login_view(request):  
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  
            return redirect("upload")  
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, "login.html")


def upload_form(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    return render(request, 'upload.html')




@login_required(login_url='/login/')  
@csrf_exempt  
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
         
        current_date = datetime.datetime.now().strftime("%Y%m%d")  
          
        formatted_file_name = f"{current_date}_{image_file.name}"
        
        original_url = f"media/{formatted_file_name}"

        
        # Skipping file storage for now
        # image_path = default_storage.save(image_file.name, image_file)
        
        # Create Image object (without storing file)
        image = Image(
            user=request.user,
            file_name=formatted_file_name,
            original_url=original_url,
            file_size=image_file.size,
            file_format=image_file.name.split('.')[-1],  
            status='uploaded'
        )
        image.save()
        saved_image = Image.objects.get(id=image.id)
        print(f"Saved image data -> ID: {saved_image.id}, Original URL: {saved_image.original_url}")

        
        return JsonResponse({
            'id': str(image.id),
            'user': str(image.user.username),
            'file_name': image.file_name, 
            'original_url': image.original_url,  
            'file_size': image.file_size,
            'file_format': image.file_format,
            'status': image.status,
            'created_at': image.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }, status=201)

    return JsonResponse({"detail": "No file uploaded."}, status=400)