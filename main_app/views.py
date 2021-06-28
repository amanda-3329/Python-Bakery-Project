from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Order, Box, Map
from .forms import OrderForm, BoxForm, OrderTrackerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shop(request):
    return render(request, 'shop.html')

def status(request, order_id):
    found_order = Order.objects.get(id=order_id)
    # print('hit the status view', order_id)
    get_status = request.POST.get('status')
    # print('$$$$$GET STATUS$$$$$', get_status)
    # found_order.status = get_status
    # form = OrderForm(found_order)
    # if form.is_valid():
    #  order=form.save(commit=False)
    found_order.status=get_status
    found_order.save()
    return redirect('detail', order_id)
    # form = OrderTrackerForm(request.POST)
    # print('==========================', form)
    # if form.is_valid():
    #     new_tracking = form.save(commit=False)
    #     new_tracking.order_id = order_id
    #     # new_tracking.save()
    #     print('***** NEW TRACKING*********', new_tracking)
    #     return redirect('detail', order_id)



# ORDER LIST:
@login_required
def order(request):
    # filter below allows user to only access their own orders.
    #if you need to view ALL orders, change to objects.all()
    orders = Order.objects.filter(user=request.user)

    context = { 'orders': orders }
    return render(request,'order/order.html', context)

    #ADMIN ORDER LIST: 
@login_required
def admin_order(request):
    # filter below allows user to only access their own orders.
    #if you need to view ALL orders, change to objects.all()
    orders = Order.objects.all()

    context = { 'orders': orders }
    return render(request,'order/order.html', context)

#ORDER DETAIL PAGE 
@login_required
def detail(request, order_id):
    found_order = Order.objects.get(id=order_id)
    print(found_order)
# THIS MAKES THE FORM SHOW UP :
    box_form = BoxForm()
    order_tracker = OrderTrackerForm()
    context = { 
        'order': found_order,
        'box_form': box_form,
        'order_tracker': order_tracker
    
     }

    

    return render(request, 'order/order_detail.html', context)
# CREATE ORDER is CUSTOMER INFO PAGE:  -----------------------
@login_required
def create_order(request):
    form = OrderForm()
    context = { 'form': form }
    if request.method == 'GET':
        return render(request, 'order/create_order.html', context)
    else:
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('detail', order.id)
        else:
            return render(request, 'order/create_order.html', context)

# Delete Order-------------
@login_required
def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('order')

def map_display(request):
    map = Map.objects.get()
    return render(request, 'about')


# Update Order-------
@login_required
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
@login_required
def box(request, order_id):
    form = BoxForm(request.POST)
    if form.is_valid():
        new_box_size = form.save(commit=False)
        new_box_size.order_id = order_id
        new_box_size.save()
        return redirect('detail', order_id)

#Delete Box:
@login_required
def delete_box(request, order_id, box_id):
    order = Order.objects.get(id=order_id)
    found_box = Box.objects.get(id=box_id)
    order.box_set.remove(found_box)

    return redirect('detail', order_id = order_id)


    
# Order Tracker Form------
@login_required
def order_tracker(request, order_id):
    form = OrderTrackerForm(request.POST)
    if form.is_valid():
        new_tracking = form.save(commit=False)
        new_tracking.order_id = order_id
        new_tracking.save()
        return redirect('detail', order_id)

# SIGN UP FORM:

def signup(request):
  error_message = ''
  if request.method == 'POST':
  
    form = UserCreationForm (request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('order')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

 