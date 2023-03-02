from django.urls import path

from main.views import other_page, index

app_name = 'main'

urlpatterns = [
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
