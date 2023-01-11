from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST.get('username', None),
            password=request.POST.get('password', None),
        )
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            message = 'Invalid username and password'
        return render(request, 'login.html', {'message': message})