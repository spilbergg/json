from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import requests

from json_pro.models import JsonUser


def get_user(request):
    user = JsonUser.objects.last()
    next_user_id = 1
    if request.method == 'POST':
        if user:
            next_user_id = user.id + 1
        result = requests.get(f'https://jsonplaceholder.typicode.com/users/{next_user_id}').json()
        if result:
            id = result['id']
            name = result['name']
            username = result['username']
            phone = result['phone']
            address_city = result['address']['city']
            JsonUser.objects.create(id=id, name=name, username=username, phone=phone, address_city=address_city)
        else:
            pass
    user_ = JsonUser.objects.all()

    return render(request, 'get_user.html', {'user': user_, 'next_user': next_user_id})


def delete_all(request):
    if request.method == 'POST':
        JsonUser.objects.all().delete()
        context = {
            'message': 'no users'
        }
    return render(request, 'get_user.html', context)



def get_json_detail(request, id):
    user = JsonUser.objects.get(id=id)
    context = {
        'user': user
    }
    return render(request, 'get_user_detail.html', context)

