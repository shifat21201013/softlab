from django.http import HttpResponse
from django.shortcuts import render
from . import forms


# Create your views here.
def add_donor(request):
    if request.method == "GET":
        form = forms.DonorForm(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponse('add successful')
    else:
        form = forms.DonorForm()
    return render(request, 'formsnew.html', {
        "form": form,
    })


# Create your views here.
