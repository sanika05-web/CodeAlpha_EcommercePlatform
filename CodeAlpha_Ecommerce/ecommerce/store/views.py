from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render, redirect
from .models import Product, Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})

@login_required
def buy(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    Order.objects.create(
        user=request.user,
        product=product
    )

    messages.success(request, "✅ Order placed successfully!")
    return redirect("my_orders")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "✅ Account created successfully. Please login.")
            return redirect('login')
        else:
            # THIS WILL SHOW THE REAL ERROR
            messages.error(request, "❌ Signup failed. See errors below.")
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})
@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "my_orders.html", {"orders": orders})
