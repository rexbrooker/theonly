from django.shortcuts import render, get_object_or_404
from django.forms import modelformset_factory
from theonly.models import MenuModel, Beverage_Serving_Size, Brewery_Graphic, Brewery, Beverage_Style, Beverage_Serving_Graphic, Beverage
from theonly.forms import MenuForm, Brewery_GraphicForm, BreweryForm, Beverage_StyleForm, Beverage_Serving_SizeForm, Beverage_Serving_GraphicForm, BeverageForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from theonly.utils import stripString

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_list_or_404
import json


def ajax_request(request):
    department_id = request.GET.get('beaverage_id')
    if department_id is None:
        return HttpResponseBadRequest()

    menu_qs = MenuModel.objects.select_related('Beverage')
    projects = get_list_or_404(menu_qs, department__id=department_id)
    data = []
    for p in projects:
        data.append({
            'id': p.id,
            'beverage_id': p.beverage_id,
            'beverage_name': p.beverage_name,
        })

    return HttpResponse(json.dumps(data), mimetype='application/json')


def theonlyView(request):
    username = request.user
    context = {'latest_word_list': 'latest_word_list', 'username': username}
    return render(request, 'theonly/theonly.html', context)


def theonlyMenuView(request):
    beverage_list = MenuModel.objects.all().order_by('menu_row', 'tap_number')
    # beverage_list = columns(beverage_list, 2)
    print(beverage_list)
    context = {'beverage_list': beverage_list}
    return render(request, 'theonly/theonlyTVMenu.html', context)


def loadBasicData(request):
    MenuModel.objects.all().delete()

    for i in range(25):
        menumodel = MenuModel()
        menumodel.brewery_id = 1
        menumodel.beverage_id = 1
        menumodel.beverage_serving_graphic_id = 2
        menumodel.beverage_serving_size_id = 1
        menumodel.tap_number = i + 1
        menumodel.id = i

        menumodel.brewery_name = "Rex Brewery"
        menumodel.beverage_name = "Rex Beer"
        menumodel.beverage_type = "Rex"
        menumodel.beverage_price_1 = 7
        menumodel.beverage_serving_size_1 = "500ml"
        menumodel.beverage_price_2 = 4
        menumodel.beverage_serving_size_2 = "325ml"
        menumodel.beverage_serving_graphic_1_id = 1
        menumodel.beverage_serving_graphic_2_id = 1
        menumodel.two_serving_sizes = True
        menumodel.save()

    return HttpResponseRedirect(reverse('updateTaps'))


def MenuUpdateTaps(request):
    data_name = 'update taps'
    all_entries = MenuModel.objects.all()

    formSet = modelformset_factory(MenuModel, form=MenuForm, max_num=25, extra=0)
    formset = formSet(request.POST or None)

    if request.method == 'POST':

        request.POST._mutable = True
        request.POST = stripString(request.POST)

        instance = get_object_or_404(MenuModel, id=request.POST['id'])
        form = MenuForm(request.POST or None, instance=instance)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
        return HttpResponseRedirect(reverse('updateTaps'))

    context = {'formset': formset, 'all_entries': all_entries, 'data_name': data_name}

    return render(request, 'theonly/update_taps.html', context)


# def stripString(POST):
#     NEWPOST = {}
#     for key in POST:
#         parts = key.split('-')
#         if parts[0] == "form" and len(parts) >= 3:
#             NEWPOST[parts[2]] = POST[key]
#         else:
#             NEWPOST[key] = POST[key]
#     return NEWPOST


def AddBrewery_GraphicView(request):
    data_name = 'Brewery Graphics'
    all_entries = Brewery_Graphic.objects.all()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Brewery_GraphicForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # newdoc = Brewery_Graphic(request.FILES['brewery_graphic'].name)
            form.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('AddBrewery_Graphic'))
    else:
        form = Brewery_GraphicForm()  # A empty, unbound form

    context = {'form': form, 'all_entries': all_entries, 'data_name': data_name}

    return render(request, 'theonly/add.html', context)


def AddBreweryView(request):
    data_name = 'Brewery'
    all_entries = Brewery.objects.all()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BreweryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()

    form = BreweryForm()
    context = {'form': form, 'all_entries': all_entries, 'data_name': data_name}
    return render(request, 'theonly/add.html', context)


def AddBeverage_StyleView(request):
    data_name = 'Beverage Style'
    all_entries = Beverage_Style.objects.all()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Beverage_StyleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
    form = Beverage_StyleForm()
    context = {'form': form, 'all_entries': all_entries, 'data_name': data_name}
    return render(request, 'theonly/add.html', context)


def AddBeverage_Serving_SizeView(request):
    data_name = 'Beverage Serving Size'
    all_entries = Beverage_Serving_Size.objects.all()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Beverage_Serving_SizeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()

    form = Beverage_Serving_SizeForm()

    context = {'form': form, 'all_entries': all_entries, 'data_name': data_name}
    return render(request, 'theonly/add.html', context)


def AddBeverage_Serving_GraphicView(request):
    data_name = 'Beverage Serving Graphic'
    all_entries = Beverage_Serving_Graphic.objects.all()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Beverage_Serving_GraphicForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            return HttpResponseRedirect(reverse('AddBeverage_Serving_Graphic'))

    form = Beverage_Serving_GraphicForm()  # A empty, unbound form

    context = {'form': form, 'all_entries': all_entries, 'data_name': data_name}
    return render(request, 'theonly/add.html', context)


def AddBeverageView(request):
    data_name = 'Beverage'
    all_entries = Beverage.objects.all()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BeverageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            return HttpResponseRedirect(reverse('AddBeverage'))
    form = BeverageForm()
    context = {'form': form, 'all_entries': all_entries, 'data_name': data_name}

    return render(request, 'theonly/add.html', context)
