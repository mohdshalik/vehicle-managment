from django.core.mail import message
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User,auth
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.edit import UpdateView



from .models import vehicle_detail
# Create your views here.
class vehicle(View):
    def get(self,request):
        all=vehicle_detail.objects.all()
        return render(request,'index.html',{'vehicles':all})



class login(View):
    def get(self,request):
        return  render(request,'login.html')
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            message.info(request, 'invalid users')
            return redirect('login')
class logout(View):
    def get(self,request):
        auth.logout(request)
        return redirect('/')
class vehicle_register(CreateView):
    model = vehicle_detail
    fields = '__all__'
    success_url = '/'

class vehicle_update(UpdateView):
    model = vehicle_detail
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url='/'

class vehicle_delete(DeleteView):
    model = vehicle_detail
    success_url='/'