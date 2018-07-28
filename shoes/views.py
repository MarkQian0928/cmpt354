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
from django.db import connection



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
    ######### Required SQL queries #########

    ######### Projection #########
    if(request.GET.get('projection')):
        temp = request.GET.get('projectBy')
        temp = mapColumnsToActualAttrNames(temp)
        try:
            results = Shoes.objects.values(temp)
        except:
            return render(request, 'shoes/searchResult.html', {"results": "",})
    #########    Aggregation     #########
    if(request.GET.get('aggregation')):
        results = Shoes.objects.raw("SELECT id, COUNT(DISTINCT brand) as Count FROM shoes_Shoes")
    ######### Nested aggregation #########
    if(request.GET.get('groupByBrand')):
        results = Shoes.objects.raw("SELECT id, brand, count(*) as Count FROM shoes_Shoes GROUP BY brand")
    if(request.GET.get('groupByCategory')):
        results = Shoes.objects.raw("SELECT id, category, count(*) as Count FROM shoes_Shoes GROUP BY category")
    if(request.GET.get('groupByRetailer')):
        results = Shoes.objects.raw("SELECT id, retailID, count(*) as Count FROM shoes_Shoes GROUP BY retailID")
    if(request.GET.get('color')):
        temp = request.GET.get('colorFilter')
        results = Shoes.objects.raw("SELECT * FROM  shoes_Shoes WHERE color = %s", [temp])
    if(request.GET.get('all')):
        results = Shoes.objects.raw('SELECT * FROM shoes_Shoes')
    ######### Deletion #########
    if(request.GET.get('delete')):
        temp = request.GET.get('deleteShoe')
        # dtemp = Shoes.objects.filter(pk=temp)
        # dtemp.delete()
        connection.cursor().execute("DELETE FROM shoes_Shoes WHERE ID= %s",[temp])
        # Shoes.objects.raw("DELETE FROM shoes_Shoes WHERE ID= %s",[temp])
        results = Shoes.objects.raw('SELECT * FROM shoes_Shoes')

    #################################
    ######### Other queries #########

    #All men's shoes
    if(request.GET.get('man')):
        # results = Shoes.objects.filter(gender='male')
        results = Shoes.objects.raw("SELECT * FROM  shoes_Shoes WHERE gender = 'male'")
    #All women's shoes
    if(request.GET.get('women')):
        results = Shoes.objects.raw("SELECT * FROM  shoes_Shoes WHERE gender = 'female'")
    #Ascending Price
    if(request.GET.get('asc')):
        results = Shoes.objects.raw("SELECT * FROM  shoes_Shoes ORDER BY price ASC")
    #Descending Price
    if(request.GET.get('desc')):
        results = Shoes.objects.raw("SELECT * FROM  shoes_Shoes ORDER BY price DESC")
    #Purchase
    if(request.GET.get('buy')):
        results = Shoes.objects.raw('SELECT * FROM shoes_Shoes')
        return render(request, 'transactions/test.html', {"results": results,})
    # Search results
    if(request.GET.get('description')): 
        searchQuery = request.GET.get('searchQuery')
        searchQuery = '%' + searchQuery + '%'
        results = Shoes.objects.raw("SELECT * FROM shoes_Shoes WHERE description LIKE %s OR category LIKE %s OR brand LIKE %s OR color LIKE %s", [searchQuery, searchQuery, searchQuery, searchQuery])

    return render(request, 'shoes/searchResult.html', {"results": results,})

def mapColumnsToActualAttrNames(str):
        if (str.lower()== "shoeid"):
            return "id";
        elif (str.lower()== "brand"):
            return "brand";
        elif (str.lower()== "category"):
            return "category";
        elif (str.lower()== "size"):
            return "size";
        elif (str.lower()== "gender"):
            return "gender";
        elif (str.lower()== "color"):
            return "color";
        elif (str.lower()== "description"):
            return "description";
        elif (str.lower()== "price"):
            return "price";
        elif (str.lower()== "availability"):
            return "numOfAvail";
        elif (str.lower()== "retailer"):
            return "retailID;"
        else:
            return ""



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

    


        
    
   
    





