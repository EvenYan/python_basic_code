from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from contact.models import PeopleInfo


def index(request):
    people_list = PeopleInfo.objects.all()
    return render(request, 'contact/index.html', context={'people_list': people_list})


def detail(request, id):
    people = PeopleInfo.objects.get(id=id)
    context = {"people": people}
    return render(request, "contact/detail.html", context=context)


def add_people(request):
    return render(request, 'contact/add_people.html')


def record(request):
    username = request.GET.get("username")
    age = request.GET.get("age")
    phone_number = request.GET.get("phone_number")
    PeopleInfo.objects.create(name=username, age=age, phone_number=phone_number)

    return HttpResponse("插入成功")