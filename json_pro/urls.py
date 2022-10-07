from django.urls import path

from json_pro.views import get_user, get_json_detail, delete_all

urlpatterns = [
    path('', get_user, name='get_user'),
    path('/<int:id>/', get_json_detail, name='get_json_detail'),
    path('/del', delete_all, name='delete_all'),
]
