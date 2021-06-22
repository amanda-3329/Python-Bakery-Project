from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Order
from .forms import OrderForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shop(request):
    return render(request, 'shop.html')

def order(request):
    orders = Order.objects.all()

    context = { 'orders': orders }
    return render(request,'order/order.html', context)

def detail(request, order_id):
    found_order = Order.objects.get(id=order_id)
    print(found_order)
    context = { 'order': found_order }

    return render(request, 'order/order_detail.html', context)
# CREATE ORDER-----------------------
def create_order(request):
    form = OrderForm()
    context = { 'form': form }
    if request.method == 'GET':
        return render(request, 'order/create_order.html', context)
    else:
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('detail', order.id)
        else:
            return render(request, 'order/create_order.html', context)

def delete_order(request, order_id):
    order =Order.objects.get(id=order_id)
    order.delete()
    return redirect('order')
