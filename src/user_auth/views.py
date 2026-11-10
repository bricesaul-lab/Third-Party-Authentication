from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from PIL import Image
import os

def signup(request):
    if request.user.is_authenticated:
        return redirect('/u')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/u')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form    = RegistrationForm()
        return render(request, 'login.html', {'form': form})


def auth_login(request):
    if request.user.is_authenticated:
        return redirect('/u')
    if request.method == 'POST':
        # Validate required fields are present
        if 'email' not in request.POST or 'password' not in request.POST:
            return redirect('/')
        
        email = request.POST['email']
        password = request.POST['password']
        
        # Basic validation
        if not email or not password:
            return redirect('/')
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/u')
        else:
            return redirect('/')
    else:
        return redirect('/')


def profile(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return redirect('/')
        else:
            print(request.user.display)
            return render(request,'profile.html')
            

def profilePic(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('/')
        
        # Check if file was uploaded
        if 'display' not in request.FILES:
            return redirect('/u')
        
        image = request.FILES['display']
        
        # File size validation (5MB limit)
        max_file_size = 5 * 1024 * 1024  # 5MB
        if image.size > max_file_size:
            return redirect('/u')  # Could add error message
        
        # File type validation
        allowed_types = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif']
        if image.content_type not in allowed_types:
            return redirect('/u')  # Could add error message
        
        # File extension validation
        allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        if not any(image.name.lower().endswith(ext) for ext in allowed_extensions):
            return redirect('/u')  # Could add error message
        
        try:
            # Validate image by trying to open it
            with Image.open(image) as test_img:
                test_img.verify()
            
            # Reset file pointer after verification
            image.seek(0)
            
            request.user.display = image
            request.user.save()
            
            def crop_center(pil_img):
                img_width, img_height = pil_img.size
                crop_height = crop_width = min([img_height, img_width])  # Fixed bug: was img_height twice
                return pil_img.crop(((img_width - crop_width) // 2,
                                    (img_height - crop_height) // 2,
                                    (img_width + crop_width) // 2,
                                    (img_height + crop_height) // 2))
            
            with Image.open(request.user.display.path) as im:
                size = 300, 300
                im = im.resize(size)
                im = crop_center(im)
                im.save(request.user.display.path)
            
            return redirect('/u')
            
        except Exception:
            # If image processing fails, remove uploaded file and redirect
            if request.user.display and os.path.exists(request.user.display.path):
                os.remove(request.user.display.path)
            return redirect('/u')
    else:
        return redirect('/u')

def delDp(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            # Check if user has a display picture before attempting to delete
            if request.user.display and os.path.exists(request.user.display.path):
                try:
                    os.remove(request.user.display.path)
                except OSError:
                    pass  # File might already be deleted or inaccessible
            request.user.display = None
            request.user.save()
            return redirect('/u')
        else:
            return redirect('/')
    else:
        return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')