from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
import json

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
            "status": True,
            "message": "Successfully Logged In!"
            # Insert any extra data if you want to pass data to Flutter
            }, status = 200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, Account Disabled."
            }, status = 401)

    else:
        return JsonResponse({
        "status": False,
        "message": "Failed to Login, check your email/password."
        }, status = 401)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password1 = data['password1']
        password2 = data['password2']
		
        try:
            form = UserCreationForm(username, password1, password2)
            form.save()
            return JsonResponse({"instance": "Registration success!"}, status=200)
        except:
            return JsonResponse({"instance": "Registration failed!"}, status=400)

    return JsonResponse({"instance": "Registration failed!"}, status=400)


@csrf_exempt
def logout_user(request):
	logout(request)
	return JsonResponse({
		"status": True,
		"message": "Logged out!"
	}, status = 200)

