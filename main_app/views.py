from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Order, Box
from .forms import OrderForm, BoxForm

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

    box_form = BoxForm()
    context = { 
        'order': found_order,
        'box_form': box_form
    
     }

    

    return render(request, 'order/order_detail.html', context)
# CREATE ORDER is CUSTOMER INFO PAGE:  -----------------------
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

# Delete Order-------------
def delete_order(request, order_id):
    order =Order.objects.get(id=order_id)
    order.delete()
    return redirect('order')

# Update Order-------
def update_order(request, order_id):
    order = Order.objects.get(id=order_id)

    if request.method == 'GET':
        form = OrderForm(instance=order)
        context = {
            'form': form
        }
        return render(request, 'order/update_order.html', context)
    else: 
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order=form.save()
            return redirect('detail', order.id)
# Add Box Size Form:

def box(request, order_id):
    form = BoxForm(request.POST)
    if form.is_valid():
        new_box_size = form.save(commit=False)
        new_box_size.order_id = order_id
        new_box_size.save()
        return redirect('detail', order_id)

#Delete Box:
def delete_box(request, order_id, box_id):
    order = Order.objects.get(id=order_id)
    found_box = Box.objects.get(id=box_id)
    order.box_set.remove(found_box)

    return redirect('detail', order_id = order_id)