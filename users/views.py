
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import UpdateView

from .forms import CustomUserCreationForm, CustomUserChangeForm


from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, render_to_response
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User



class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

<<<<<<< HEAD
# class UpdateInfo(generic.CreateView):
#     @login_required
    # user_form = CustomUserChangeForm(instance=user)
    # form_class = CustomUserChangeForm
    # template_name = 'update/base.html'
    # 
# class UpdateInfo(generic.CreateView):
def change(request, template_name = 'update/base.html'):
   
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST,instance=request.user)
        # form = UserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # success_url = reverse_lazy('home')
        #   url = reverse ('home')
            return HttpResponseRedirect('/')
    else:
        form = CustomUserChangeForm(instance=request.user)
    # page_title = _('Edit user names')
    return render(request, template_name, {'form': form})


# class UpdateInfo (UpdateView):
#     model = CustomUser
#     # fields = ('username', 'email', 'first_name', 'last_name')
#     form_class = CustomUserChangeForm
#     template_name = 'update/base.html'
    # success_url = reverse_lazy('login')
    # slug_flied = 'username'
    # slug_url_kwarg = 'not_slug'


=======
class UpdateInfo(generic.CreateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('login')
    template_name = 'updateInfo.html'
>>>>>>> 9f7f047a4a7b98f942c7baadf01ca86af883b03b
