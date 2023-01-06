from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Topic
from .form import ProductForm

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    page = 'login'
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exits')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Incorrect username or password')


    context = {'page':page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
    
    context = {'form': form}
    return render(request, 'base/login_register.html', context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else '' 
    products = Product.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    
    # products = Product.objects.all()
    context = {'products':products}
    return render(request, 'base/home.html', context)



def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product':product}
    return render(request, 'base/product.html', context)


@login_required(login_url='/login')
def createProduct(request):
    form = ProductForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
    if request.method == 'POST':
        
        Product.objects.create(
            host=request.user,
            topic=topic,
            image=request.POST.get('image'),
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            miles=request.POST.get('miles'),
            location=request.POST.get('location'),
            used_or_new=request.POST.get('used_or_new'),
            price=request.POST.get('price'),
            engine_type=request.POST.get('engine_type'),
            Transmission=request.POST.get('Transmission'),
            fuel_type=request.POST.get('fuel_type'),
            interior_color=request.POST.get('interior_color'),
            Exterior_color=request.POST.get('Exterior_color'),
            vehicle_id=request.POST.get('vehicle_id')
        )        
        return redirect('home')
        # form = ProductForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('home')
        #     name = form.cleaned_data['name']
        #     price = form.cleaned_data['price']
        #     product = Product(name=name, price=price))


    context = {'form':form, 'topics':topics}
    return render(request, 'base/product_form.html', context)






def sellCars(request):
    return render('')

def help(request):
    return HttpResponse('This the Help section')

def aboutUs(request):
    return HttpResponse('This the About-us section')
    