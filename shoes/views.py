from django.shortcuts import render
from django.views import generic, View
from django.views.generic import ListView
from .forms import ShoesCreationForm
from django.contrib.auth.decorators import login_required
from users.models import CustomUser, Retailer
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from .models import Shoes
from .forms import ShoesCreationForm
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, render_to_response, redirect
from django.urls import reverse_lazy


class ShoesListView(ListView):
    model = Shoes
    # paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddShoes(generic.CreateView):
    form_class = ShoesCreationForm
    template_name = 'shoes/add.html'
    success_url = '/shoes/list'
    

# def AddShoes(request, template_name = 'shoes/add.html'):
#     if request.user.is_authenticated:
#         try:
#             retailerCheck = Retailer.objects.get(customUser=request.user)
            
#         except Retailer.DoesNotExist:
#             temp =Retailer(customUser = request.user)
#             temp.save()
#             return HttpResponseRedirect('shoes/notRetailer.html')
#             # form_class = ShoesCreationForm
#             # template_name = 'shoes/add.html'
#             # success_url = reverse_lazy('login')
#         if retailerCheck.retailerOrNot == True:
#             # Shoes(retailID = retailerCheck)
#             if request.method == "POST":
#                 Shoes(retailID = retailerCheck)
#                 form = ShoesCreationForm (request.POST)
#                 if form.is_valid():
#                     shoe = form.save(commit =False)
#                     shoe.save()
#                     return HttpResponseRedirect('shoes/list')
#             else:
#                 form = ShoesCreationForm(instance= retailerCheck)
#                 return render(request, template_name, {'form': form})


#         # return HttpResponseRedirect('/')
#     else:
        
#         return HttpResponseRedirect('/unauthorized.html')

    


        
    
   
    





