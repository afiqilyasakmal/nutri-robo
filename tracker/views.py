from django.shortcuts import render
from tracker.models import CalorieTracker, SleepTracker
from tracker.models import WaterTracker
from tracker.models import ExerciseTracker
from django.shortcuts import redirect
import datetime
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# TODO: Create your views here. 

@login_required(login_url='/login/')
def show_tracker(request):
    calorie_item = CalorieTracker.objects.order_by('-date')
    water_item = WaterTracker.objects.order_by('-date')
    exercise_item = ExerciseTracker.objects.order_by('-date')
    sleep_item = SleepTracker.objects.order_by('-date')
    context = {
        'calorie_item': calorie_item,
        'water_item': water_item,
        'exercise_item': exercise_item,
        'sleep_item': sleep_item,
        'username': request.user,
    }
    return render(request, "tracker.html", context)

@login_required(login_url='/login/')
@csrf_exempt
def add_calorie(request):
	if request.method == "POST":
		calorie = request.POST.get("calorie")
		description = request.POST.get("description")
		date= request.POST.get("date")
		time= request.POST.get("time")
		CalorieTracker.objects.create(time=time, date=date, calorie=calorie, description=description, user=request.user)
		return HttpResponse()
	else:
		return redirect('tracker:show_tracker')

@login_required(login_url='/login/')
@csrf_exempt
def add_water(request):
	if request.method == "POST":
		water = request.POST.get("water")
		description = request.POST.get("description")
		date= request.POST.get("date")
		time= request.POST.get("time")
		WaterTracker.objects.create(time=time, date=date, water=water, description=description, user=request.user)
		return HttpResponse()
	else:
		return redirect('tracker:show_tracker')

@login_required(login_url='/login/')
@csrf_exempt
def add_exercise(request):
	if request.method == "POST":
		exercise = request.POST.get("exercise")
		description = request.POST.get("description")
		date= request.POST.get("date")
		time= request.POST.get("time")
		ExerciseTracker.objects.create(time=time, date=date, exercise=exercise, description=description, user=request.user)
		return HttpResponse()
	else:
		return redirect('tracker:show_tracker')

@login_required(login_url='/login/')
@csrf_exempt
def add_sleep(request):
    if request.method == "POST":
        sleephours = request.POST.get("sleephours")
        sleepminutes = request.POST.get("sleepminutes")
        description = request.POST.get("description")
        date= request.POST.get("date")
        time= request.POST.get("time")
        SleepTracker.objects.create(time=time, date=date, sleephours=sleephours, sleepminutes=sleepminutes, description=description, user=request.user)
        return HttpResponse()
    else:
        return redirect('tracker:show_tracker')

def show_calorie_json(request):
    calorie_item = CalorieTracker.objects.all()
    return HttpResponse(serializers.serialize("json", calorie_item), content_type="application/json")

def show_water_json(request):
    water_item = WaterTracker.objects.all()
    return HttpResponse(serializers.serialize("json", water_item), content_type="application/json")

def show_exercise_json(request):
    exercise_item = ExerciseTracker.objects.all()
    return HttpResponse(serializers.serialize("json", exercise_item), content_type="application/json")

def show_sleep_json(request):
    sleep_item = SleepTracker.objects.all()
    return HttpResponse(serializers.serialize("json", sleep_item), content_type="application/json")

def delete_calorie(request, id):
	calorie_item = CalorieTracker.objects.filter(pk = id)
	calorie_item.delete()
	return redirect('tracker:show_tracker')

def delete_water(request, id):
	water_item = WaterTracker.objects.filter(pk = id)
	water_item.delete()
	return redirect('tracker:show_tracker')

def delete_exercise(request, id):
	exercise_item = ExerciseTracker.objects.filter(pk = id)
	exercise_item.delete()
	return redirect('tracker:show_tracker')

def delete_sleep(request, id):
	sleep_item = SleepTracker.objects.filter(pk = id)
	sleep_item.delete()
	return redirect('tracker:show_tracker')
