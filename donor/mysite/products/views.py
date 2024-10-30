from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProductSearchForm
from .models import Product
from . import forms


# Create your views here.
def add_product(request):
    if request.method == "GET":
        form = forms.ProductForm(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponse('add successful')
    else:
        form = forms.ProductForm()
    return render(request, 'forms.html', {
        "form": form,
    })


def product_search(request):
    if request.method == 'GET':
        form = ProductSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query')
            results = Product.objects.filter(blood_group__icontains=search_query)
            return render(request, 'search_results.html', {'results': results})
    else:
        form = ProductSearchForm()
    return render(request, 'home2.html', {'form': form})