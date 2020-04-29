from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.db.models import Q,F
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from durianGarden.settings import EMAIL_HOST_USER

from main.forms import *
from main.models import *
from main.query_functions import *
from main.get_data import *

from account.models import *
from account.forms import *

from .decorators import unauthenticated_user, allowed_users, admin_only

import MySQLdb
import datetime

results_list = []

@login_required(login_url='login')    
def dashboard(request):
    #CARD 1
    total_items = 0
    count1= Spareparts.objects.all().count()
    count2= Tools.objects.all().count()
    count3= Stationery.objects.all().count()
    count4= Consumables.objects.all().count()
    count5= Fungicide.objects.all().count()
    count6= Fertilizer.objects.all().count()
    count7= Surfacetant.objects.all().count()
    count8= Herbicide.objects.all().count()
    count9= Pesticide.objects.all().count()
    count10= Irrigation.objects.all().count()

    total_items = count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8 + count9 + count10
    
    #CARD 2
    

    #CARD 3
    totalPurchases = 0
    countP = Purchasing.objects.all().count()
    totalPurchases = countP

    #CARD 4
    item_lowStock = 0
    low1 = Tools.objects.all().filter(quantity__lte=F('threshold')).count()
    low2 = Consumables.objects.all().filter(quantity__lte=F('threshold')).count()
    low3 = Fungicide.objects.all().filter(quantity__lte=F('threshold')).count()
    low4 = Fertilizer.objects.all().filter(quantity__lte=F('threshold')).count()
    low5 = Surfacetant.objects.all().filter(quantity__lte=F('threshold')).count()
    low6 = Herbicide.objects.all().filter(quantity__lte=F('threshold')).count()
    low7 = Pesticide.objects.all().filter(quantity__lte=F('threshold')).count()
    low8 = Irrigation.objects.all().filter(quantity__lte=F('threshold')).count()
    low9 = Spareparts.objects.all().filter(quantity__lte=F('threshold')).count()
    low10 = Stationery.objects.all().filter(quantity__lte=F('threshold')).count()

    item_lowStock = low1 + low2 + low3 + low4 + low5 + low6 + low7 + low8 + low9 + low10

    irrigation_lowStock, plantation_lowStock, spareparts_lowStock = get_low_stock_results()
    isIrrigationLow = len(irrigation_lowStock) > 0
    isPlantationLow = len(plantation_lowStock) > 0
    isSparepartsLow = len(spareparts_lowStock) > 0

    context = {
        "dashboard": "active",
        'total_items': total_items,
        'item_lowStock': item_lowStock,
        'totalPurchases': totalPurchases,
        'irrigation_results': irrigation_lowStock,
        'plantation_results': plantation_lowStock,
        'spareparts_results': spareparts_lowStock,
        'isIrrigationLow': isIrrigationLow,
        'isPlantationLow': isPlantationLow,
        'isSparepartsLow': isSparepartsLow,
    }
    return render(request, 'main/dashboard.html',context)

@login_required(login_url='login') 
def index(request):

    iri_cat_list = get_category_subcat(Irrigation_Tables)
    plant_cat_list = get_category_subcat(Plantation_Tables)
    vehicle_cat_list  = get_category_subcat(Vehicle_Tables)

    iri_table = iri_cat_list[0]
    plant_table = plant_cat_list[0]
    vehicle_table = vehicle_cat_list[0]

    context = {"index": "active", 'iri_table_label': iri_table, 'plant_table_label': plant_table, 'vehicle_table_label': vehicle_table}
    return render(request, 'main/index.html',context)

@login_required(login_url='login') 
def purchasing(request):
    category = 'purchasing'
    subcategory = 'Purchasing'
    
    #Query variables
    query_results = Purchasing.objects.all()
    query_count = Purchasing.objects.all().count()

    #No of Queries
    a = 5
    if request.method == 'POST':
       a = request.POST['drop1']

    #Search query
    query = request.GET.get("q")
    if request.method == 'GET':
        query_results = purchasing_query(query_results, query)

    #Paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(query_results, a)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index -5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    results = get_all_results(Purchasing)
    cat_list = ['Purchasing']

    context = {
        'query_results': query_results,
        'query_count': query_count,
         'items': items,
         'a': a,
         'pag_template': "main/pagination.html",
         'results': results,
         'cat_list': cat_list, 
         'label':"Purchasing", 
         'subcategory' : subcategory, 
         'category': category,
         
        }
    return render(request, 'main/purchasing.html',context)

@login_required(login_url='login')  
def irrigation(request, subcategory):

    category = 'Irrigation_Tables'

    cat_list = get_category_subcat(Irrigation_Tables)
    results = get_all_results(findTable(subcategory))
    results = get_supplier_name(subcategory, results)

    context = {'results': results,'cat_list': cat_list, 'subcategory': subcategory, 'category': category}

    return render(request, 'main/tables_base.html', context)

@login_required(login_url='login') 
def plantation(request, subcategory):

    category = 'Plantation_Tables'

    cat_list = get_category_subcat(Plantation_Tables)
    results = get_all_results(findTable(subcategory))
    results = get_supplier_name(subcategory, results)

    context = {'results': results,'cat_list': cat_list, 'subcategory': subcategory, 'category': category}

    return render(request, 'main/tables_base.html',context)

@login_required(login_url='login') 
def vehicle(request, subcategory):

    category = 'Vehicle_Tables'

    cat_list = get_category_subcat(Vehicle_Tables)
    results = get_all_results(findTable(subcategory))
    if subcategory == 'Spareparts':
        results = get_supplier_name(subcategory, results)
    
    context = {'results': results, 'cat_list': cat_list, 'subcategory': subcategory, 'category': category}
    return render(request, 'main/tables_base.html',context)

@login_required(login_url='login') 
def orderView(request):
    if request.method == 'GET':
        form = OrderForm()
    else:
        form = OrderForm(request.POST)
        if form.is_valid():
            subject = "DurianGarden order on " + str(datetime.date.today())
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, EMAIL_HOST_USER , [email], fail_silently = False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('main:success')
    return render(request, 'main/order.html',{'form': form})

@login_required(login_url='login') 
def successView(request):

    return HttpResponse('Success! Thank you for your order.')

@login_required(login_url='login') 
def supplier(request):
    category = 'supplier'
    subcategory = 'Supplier'
    results= get_all_results(Supplier)
    cat_list = ['Supplier']

    context = {"supplier": "active",'results': results,'cat_list': cat_list, 'label':"Supplier", 'subcategory' : subcategory, 'category': category}
    return render(request, 'main/supplier.html', context)

@login_required(login_url='login') 
def addItem(request, category, subcategory):
    # Create and update database

    if request.method != 'POST':
        form_object = findForm(subcategory)  # find the specific form according to the string value passed
        # No data submitted; create a blank form
        form = form_object()
    else:
        form_object = findForm(subcategory)  # find the specific form according to the string value passed
        # POST data submitted; process data
        form = form_object(data=request.POST)
        if form.is_valid():
            form.save()
            if subcategory == 'Purchasing' or subcategory == 'Supplier':
                return redirect(f'/{category}/')
            else:
                return redirect(f'/{category}/{subcategory}')

    context = {'form': form, 'form_name': subcategory}
    return render(request, 'main/addItem.html', context)

@login_required(login_url='login') 
def userprofile(request):
    if request.user.is_superuser == False:
        staff = request.user.staff
        form = StaffForm(instance=staff)

    if request.method =='POST':
        form = StaffForm(request.POST, request.FILES, instance = staff)
        if form.is_valid:
            form.save()

    if request.user.is_superuser:
        return render(request, 'main/userprofile.html', {"userprofile": "active"})
    return render(request, 'main/userprofile.html',{"userprofile": "active",'form': form,})
    
@login_required(login_url='login') 
def delete_entry(request, pk=None, subcategory=None, category=None):
    if request.method== "POST" and "delete_this" in request.POST:
        table_to_del = findTable(subcategory)

        objects = table_to_del.objects.get(pk=pk)
        objects.delete()
        if subcategory == 'Purchasing' or subcategory == 'Supplier':
            return redirect(f'/{category}/')
        else:
            return redirect(f'/{category}/{subcategory}')

@login_required(login_url='login') 
def update_entry(request, category=None, subcategory=None, pk=None):
    form_to_update = findForm(subcategory)
    model_object = findTable(subcategory)
    instance_lol = get_object_or_404(model_object, pk=pk)
    print(f'Instance is {instance_lol}')
    
    if request.method == "POST":
        some_form = form_to_update(request.POST or None ,instance = instance_lol)
        if some_form.is_valid():
            some_form.save()

            if subcategory == 'Purchasing' or subcategory == 'Supplier':
                return redirect(f'/{category}/')
            else:
                return redirect(f'/{category}/{subcategory}')
    else:
        some_form = form_to_update(instance = instance_lol)

    context = {'form': some_form, 'form_name':subcategory}

    return render(request, 'main/updateItem.html', context)
