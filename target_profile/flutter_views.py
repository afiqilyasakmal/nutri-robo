from django.contrib.auth.models import User
from django.contrib.auth import BACKEND_SESSION_KEY, HASH_SESSION_KEY, SESSION_KEY, authenticate, login, logout
from django.http import JsonResponse, response
import json
from django.utils.dateparse import parse_date
from django.views.decorators.csrf import csrf_exempt
from time import sleep

from django.http import HttpResponse
from django.core import serializers

from . import  models as mdl
from target_profile.forms import FormPhysicalInfo, FormProfile

from target_profile.models import PhysicalInfo, Profile

@csrf_exempt
def show_user_profile(request, username):
    user = User.objects.get(username = username)
    sleep(0)
    if user is not None:
        data_feedback = Profile.objects.filter(user = user)
        return HttpResponse(serializers.serialize("json", data_feedback), content_type="application/json")
    else:
        return JsonResponse({}, status=404)

@csrf_exempt
def show_user_target(request, username):
    user = User.objects.get(username = username)
    sleep(0)
    if user is not None:
        data_feedback = PhysicalInfo.objects.filter(user = user)
        return HttpResponse(serializers.serialize("json", data_feedback), content_type="application/json")
    else:
        return JsonResponse({}, status=404)

@csrf_exempt
def update_profile(request): ####    
    form = FormProfile(request.POST)
    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        return JsonResponse(
        {
            "status": True,
            "message": "Profile successfully updated!",
        }, status = 200)
    else:
        return JsonResponse(
            {
                "status": False,
                "message": "Failed to update profile!",
                "details": form.errors
            }, status = 400)

@csrf_exempt
def update_target(request): ####    
    form = FormPhysicalInfo(request.POST)
    if form.is_valid():
        target = form.save(commit=False)
        target.user = request.user
        target.save()
        return JsonResponse(
        {
            "status": True,
            "message": "Target health successfully updated!",
        }, status = 200)
    else:
        return JsonResponse(
            {
                "status": False,
                "message": "Failed to update target health!",
                "details": form.errors
            }, status = 400)

# @csrf_exempt
# def profile_flutter(request, username):
#     print(username+"-------")
#     # data = json.loads(request.body)
#     user = User.objects.get(username=username)
#     sleep(0)
#     if user is not None:
#         print(user.username)

#         # profile = mdl.Profile.objects.get(user=user)        
#         # #bod = profile.birthday

#         # return JsonResponse({
#         #     "username": username,
#         #     "bod": profile.name or "belum diatur",
#         #     "bio": profile. or "belum diatur",
#         #     "email": profile.email
#         # }, status=200)
#         try:
#             profile = mdl.Profile.objects.get(
#                 user = request.user
#             )
#         except mdl.Profile.MultipleObjectsReturned:
#             profile = mdl.Profile.objects.filter(
#                 user = request.user
#             ).last()
#         except mdl.Profile.DoesNotExist:
#             profile = "Belum diatur"
#         return HttpResponse(serializers.serialize("json", profile), content_type="application/json")
#     else:
#         return JsonResponse({}, status = 404)
    
# @csrf_exempt
# def target_flutter(request, username):
#     print(username+"-------")
#     # data = json.loads(request.body)
#     user = User.objects.get(username=username)
#     sleep(0)
#     if user is not None:
#         print(user.username)

#         # profile = mdl.Profile.objects.get(user=user)        
#         # #bod = profile.birthday

#         # return JsonResponse({
#         #     "username": username,
#         #     "bod": profile.name or "belum diatur",
#         #     "bio": profile. or "belum diatur",
#         #     "email": profile.email
#         # }, status=200)
#         try:
#             target = mdl.PhysicalInfo.objects.get(
#                 user = request.user
#             )
#         except mdl.PhysicalInfo.MultipleObjectsReturned:
#             target = mdl.PhysicalInfo.objects.filter(
#                 user = request.user
#             ).last()
#         except mdl.PhysicalInfo.DoesNotExist:
#             target = "Belum diatur"
#         return HttpResponse(serializers.serialize("json", target), content_type="application/json")
#     else:
#         return JsonResponse({}, status = 404)



# @csrf_exempt
# def coru_profile_flutter(request):
#     data = json.loads(request.body)
#     username = data['username']
#     user = User.objects.get(username=username)
#     print(data['email'])
#     sleep(0)
#     # return JsonResponse({}, status=200)
#     if user is not None:
#         user_profile = mdl.Profile.objects.filter(user=user)  # Mendapatkan profile berdasarkan user
#         # user_profile.birthday = parse_date(data['bod'][:10])
#         # user_profile.bio = data['bio']
#         user_profile.name = data['name']
#         user_profile.phone = data['phone']
#         user_profile.email = data['email']
#         user_profile.role = data['role']
#         user_profile.save() 
#         return JsonResponse({}, status=200)
#     else:
#         return JsonResponse({}, status=404)

# @csrf_exempt
# def coru_target_flutter(request):
#     data = json.loads(request.body)
#     username = data['username']
#     user = User.objects.get(username=username)
#     print(data['email'])
#     sleep(0)
#     # return JsonResponse({}, status=200)
#     if user is not None:
#         user_profile = mdl.Profile.objects.filter(user=user).last()  # Mendapatkan profile berdasarkan user
#         # user_profile.birthday = parse_date(data['bod'][:10])
#         # user_profile.bio = data['bio']
#         user_profile.name = data['name']
#         user_profile.phone = data['phone']
#         user_profile.email = data['email']
#         user_profile.role = data['role']
#         user_profile.save() 
#         return JsonResponse({}, status=200)
#     else:
#         return JsonResponse({}, status=404)