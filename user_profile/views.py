
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.views.generic import ListView
from user_profile.forms import PhysicalInfoForm, ProfileForm
from django.contrib.auth.models import User

from .models import Profile
from .models import PhysicalInfo
import datetime
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def logout_user(request):
    logout(request)
    return redirect('landingPage:show_landingPage')

@login_required(login_url='/login/')
def create_profile(request):
    user_id = request.user.id
    user = request.user
    username = request.user.username
    profile = Profile.objects.filter(user = user)
    if not profile:
        
        form = ProfileForm()
        if request.method == "POST":
            form = ProfileForm(request.POST)
            if form.is_valid():
                profile = Profile.objects.create(user=request.user, name = request.POST['name'], phone=request.POST['phone'], email=request.POST['email'], role = request.POST['role'])
                profile.save()
                messages.success(request, "Berhasil menambahkan data diri")
                return redirect('user_profile:show_profile')
        context = {'profile_form' : form}
        return render(request, 'create_profile.html', context)
    else:
        show_profile(request)
        return redirect('user_profile:show_profile')


def show_profile(request):
    username = request.user.username
    user = request.user
    usr_profile = Profile.objects.filter(user = user)
    context = {
        'usr_profile' : usr_profile,

        'username' : username
    }
    return render(request, 'data_diri.html', context)


class PhysicalInfoView(ListView):
    model = PhysicalInfo
    template_name = 'target.html'
    context_object_name = 'physicals_info'

class CreateTarget(View):
    def get(self, request):
        gender1 = request.GET.get('gender')
        weight1 = request.GET.get('weight')
        height1 = request.GET.get('height')
        age1 = request.GET.get('age')
        calories1 = 0
        exercise1 = 0
        sleep_time = ""

        # Rumus berdasarkan BMR
        if (gender1 == 'Male'):
            calories1 = (88.4 + 13.4 * weight1) + (4.8 * height1) - (5.68 * age1)
        else :
            calories1 = (447.6 + 9.25 * weight1) + (3.10 * height1) - (4.33 * age1)
    
        # Berdasarkan penelitian
        if (7 <= age1 <= 18):
            exercise1 = 60 #minutes/day
        elif (19 <= age1 <= 30):
            exercise1 = 40 #minutes/day
        elif (31 <= age1 <= 45):
            exercise1 = 30 #minutes/day
        elif (46 <= age1 <= 60):
            exercise1 = 15 #minutes/day
    
        # Berdasarkan penelitian
        if (1 <= age1 < 3):
            sleep_time = "12 - 14"
        elif (3 <= age1 < 6):
            sleep_time = "10"
        elif (6 <= age1 < 12):
            sleep_time = "8 - 9"
        elif (12 <= age1 < 18):
            sleep_time = "7 - 8"
        elif (18 <= age1 < 40):
            sleep_time = "7"
        elif (age1 >= 40 ):
            sleep_time = "6"

        #bb 35 kg = 1500 ml, untuk setiap 1 kg bb setelahnya nambah 40ml
        water1 = (weight1 - 35) * 40 + 1500


        phy_info = PhysicalInfo.objects.create(user=request.user, gender = gender1, 
                        weight = weight1, height = height1, age = age1, calories = calories1,
                        water = water1, sleep = sleep_time, exercise = exercise1)
        phy_info.save

        phy_user = {
            'gender': gender1, 
            'weight': weight1, 
            'height': height1,
            'age': age1,
            'calories' : calories1,
            'exercise' : exercise1,
            'sleep' : sleep_time,
            'water' : water1

            }

        context = {
            'phy_user' : phy_user
        }
        return JsonResponse(context)



