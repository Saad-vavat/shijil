

from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login , logout

from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
        if request.user.is_authenticated:
            return redirect('info')
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('info')
            else:
                messages.info(request, 'Username or Password is incorrect')


        context={}
        return render(request, 'index.html',context)


# def registerPage(request):
#     if request.user.is_authenticated:
#         return redirect('info')
#     else:
#         form = CreateUserForm()
#         if request.method == "POST":
#             form = CreateUserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get('username')
#                 messages.success(request, 'Account was created for ' + user)
#                 return redirect('home')

#         context={'form':form}
#         return render(request, 'register.html',context)


@login_required(login_url='home')
def logoutUser(request):
    logout(request)
    return redirect('home')



