# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product, GymClass, CustomUser
import json
from django.http import JsonResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # ✅ corrected
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'mainapp/login.html', {'error': 'Invalid credentials'})
    return render(request, 'mainapp/login.html')




@login_required(login_url='login')
def home_view(request):
    return render(request, 'mainapp/home.html', {'user': request.user})



def shop_view(request):
    category = request.GET.get('category')
    products = Product.objects.filter(category=category) if category else Product.objects.all()
    categories = Product.CATEGORY_CHOICES
    return render(request, 'mainapp/shop.html', {'products': products, 'categories': categories})



def classes_list(request):
    all_classes = GymClass.objects.all()
    return render(request, 'mainapp/classes.html', {'classes': all_classes})



def attend_class(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        class_id = data.get('class_id')

        try:
            class_obj = GymClass.objects.get(id=class_id)
            request.user.classes_attended.add(class_obj)
            request.user.level_up()
            return JsonResponse({'message': 'Successfully attended class!'})
        except GymClass.DoesNotExist:
            return JsonResponse({'message': 'Class not found.'}, status=404)

    return JsonResponse({'message': 'Invalid request'}, status=400)


def logout_view(request):
    logout(request)
    return redirect('login')
