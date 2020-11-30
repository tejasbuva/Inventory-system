from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from .filters import ProductFilter
from .forms import ProductForm, ProductSearchForm
from django.core.paginator import Paginator
from .models import Product


def home(request):
    return render(request, "home.html")


def login_view(request):  # Function for the Login
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('employeeDashboard')
    else:
        form = AuthenticationForm()
    title = 'Login'
    context = {
        "title": title,
        "form": form,
    }
    return render(request, 'login.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        return redirect('home')


@login_required(login_url="login")
def dashboard(request):
    title = 'Dashboard'
    form = ProductSearchForm(request.POST or None)
    if request.user.is_superuser:
        # products = Product.objects.all().order_by('Purchase_Date')
        products = ProductFilter(request.GET, queryset=Product.objects.all().order_by('Purchase_Date')).qs
        context = {
            "title": title,
            "products": products,
            "form": form,
        }
    elif str(request.user.groups.get()) == "Accountant":
        # products = ProductFilter(request.GET, queryset=Product.objects.all().order_by('Purchase_Date')).qs
        products = ProductFilter(request.GET, queryset=Product.objects.exclude(Product_Group=request.user.groups.get()).order_by('Purchase_Date')).qs
        context = {
            "title": title,
            "products": products,
            "form": form,
        }
    else:
        # products = Product.objects.filter(Product_Group=request.user.groups.get()).order_by('Purchase_Date')
        products = ProductFilter(request.GET, queryset=Product.objects.filter(Product_Group=request.user.groups.get()).order_by('Purchase_Date')).qs
        context = {
            "title": title,
            "products": products,
            "form": form,
        }

    if request.method == 'POST':
        products = Product.objects.all().order_by('Purchase_Date').filter(
            Product_Name__icontains=form['Product_Name'].value(), Serial_No__icontains=form['Serial_No'].value())
        context = {
            "title": title,
            "products": products,
            "form": form,
        }
    return render(request, 'dashboard.html', context)


@login_required(login_url="login")
def additems(request):
    title = 'Add New Product'
    form = ProductForm(request.POST or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.User_Name = request.user
        product.Product_Group = request.user.groups.get()
        product.save()
        return redirect('/dashboard')
    context = {
        "title": title,
        "form": form,
        "image": image,
    }
    return render(request, 'additems.html', context)


@login_required(login_url="login")
def summary(request):
    title = 'Summary'
    product_count = Product.objects.all().count()
    accountant_count = Product.objects.filter(Product_Group=Group.objects.filter(name="Accountant")[0]).count()
    manufacturer_count = Product.objects.filter(Product_Group=Group.objects.filter(name="Manufacturer")[0]).count()
    rnd_count = Product.objects.filter(Product_Group=Group.objects.filter(name="RnD")[0]).count()
    sales_count = Product.objects.filter(Product_Group=Group.objects.filter(name="Sales")[0]).count()

    context = {
        "title": title,
        "product_count": product_count,
        "accountant_count": accountant_count,
        "manufacturer_count": manufacturer_count,
        "rnd_count": rnd_count,
        "sales_count": sales_count,
    }
    return render(request, 'summary.html', context)


@login_required(login_url="login")
def product_edit(request, id=None):
    instance = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('/dashboard')
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, "additems.html", context)


@login_required(login_url="login")
def product_delete(request, id=None):
    instance = get_object_or_404(Product, id=id)
    instance.delete()
    return redirect('/dashboard')


def my_account(request):
    items = Product.objects.all()
    p7 = Paginator(items, 10)
    page = request.GET.get('page')
    products = p7.get_page(page)
    return render(request, 'dashboard.html', {'products':products})