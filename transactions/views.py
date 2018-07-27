from django.shortcuts import render, HttpResponseRedirect
from shoes.models import Shoes
from users.models import CustomUser
from .models import transactionHistory
from django.views.generic import ListView
from django.contrib.auth.models import User

def test(request):
    if(request.GET.get('buy')):
        results = Shoes.objects.all()

    return render(request, 'transactions/test.html', {"results": results,})

def tranDetails(request):
    if(request.GET.get('check')):
        temp1 = request.GET.get('shoeID')
        temp2 = request.GET.get('cusID')
        shoeDetail = Shoes.objects.filter(pk=temp1).values('brand', 'category', 'size', 'gender', 'color',)
        cusDetail = CustomUser.objects.filter(pk=temp2).values('username', 'email')
    return render(request, 'transactions/transaction_detail.html', {"shoeDetail": shoeDetail, "cusDetail": cusDetail})



def tranHistory(request):
    if request.user.is_authenticated:
        if(request.GET.get('buy')):
            temp1 = request.GET.get('shoeID')
            temp2 = request.GET.get('num')
            temp3 = request.GET.get('price')
            temp4 = request.user.pk
            temp5 = request.GET.get('originN')
            sSave = transactionHistory(numPurchased=int(temp2), shoeName=temp1, customerName=temp4, price =temp3,)
            sSave.save()
            temp6 = int(temp5)-int(temp2)
            shoeUpdate = Shoes.objects.filter(pk=temp1).update(numOfAvail=temp6)
            # shoeUpdate.save()
        
            results = transactionHistory.objects.filter(customerName=temp4)
            shoeResult = Shoes.objects.all()
        return render(request, 'transactions/test.html', {"results": results, "shoeResult": shoeResult})
    else:
        return HttpResponseRedirect('/users/login')



class TranListView(ListView):
    model = transactionHistory
    # paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# def joinquery(request):