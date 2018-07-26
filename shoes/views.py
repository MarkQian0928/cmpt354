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

from django.db.models import Avg, Count, Max



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
    
# class SelectView(ListView):
#     model = Shoes

def shoeQuery (request):
    if(request.GET.get('color')):
        temp = request.GET.get('colorFilter')
        results = Shoes.objects.filter(color=temp)
        # context = super().get_context_data()
        # return results
    if(request.GET.get('price')):
        results = Shoes.objects.all().aggregate(Max('price'))
    if(request.GET.get('all')):
        results = Shoes.objects.all()
    if(request.GET.get('projection')):
        results = Shoes.objects.values('brand', 'size', 'price')
    if(request.GET.get('nested')):
        results = Shoes.objects.all().values('retailID',).annotate(num_shoes=Count('price')).order_by('num_shoes')
    if(request.GET.get('delete')):
        temp = request.GET.get('deleteShoe')
        dtemp = Shoes.objects.filter(pk=temp)
        dtemp.delete()
        results = Shoes.objects.all()
    


    return render(request, 'shoes/searchResult.html', {"results": results,})





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

    


        
    
   
    





