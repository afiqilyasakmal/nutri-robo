from importlib.resources import contents
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from partFAQ.models import FAQContent
# Create your views here.

def mainPageFAQ(request):
    faqs = FAQContent.objects.all()
    contents = {
        'faqs': faqs
    }
    return render(request, 'mainPageFAQ.html', contents)

def getFAQContent(request):
    if request.method == 'GET':
        data = FAQContent.objects.all()
        test = FAQContent.objects.filter(question__contains='quest')
        # print(data)
        return HttpResponse(serializers.serialize("json", test ), content_type="application/json")

def showFAQbyId(request, id):
    faq = FAQContent.objects.get(pk=id)
    contents = {
        'faq': faq
    }
    return render(request, 'showFAQbyId.html', contents)


