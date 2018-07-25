
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import UpdateView

from .forms import CustomUserCreationForm, CustomUserChangeForm, RetailerForm


from django.contrib.auth.decorators import login_required
from .models import CustomUser, Retailer
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, render_to_response
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User



class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def change(request, template_name = 'update/base.html'):
    try:
        retailerID = Retailer.objects.get(customUser=request.user)
    except Retailer.DoesNotExist:
        temp =Retailer(customUser = request.user)
        temp.save()
        retailerID = Retailer.objects.get(customUser=request.user)
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST,instance=request.user, prefix='form')
        rForm = RetailerForm(request.POST, instance = retailerID, prefix = 'rForm')
        if form.is_valid() and rForm.is_valid():
            user = form.save(commit=False)
            retailer = rForm.save(commit=False)
            user.save()
            retailer.save()

            return HttpResponseRedirect('/')
    else:
        form = CustomUserChangeForm(instance=request.user, prefix='form')
        rForm = RetailerForm(instance=retailerID, prefix = 'rForm')
    return render(request, template_name, {'form': form, 'rForm': rForm})




