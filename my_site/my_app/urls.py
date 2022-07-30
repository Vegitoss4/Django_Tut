from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index') #/my_apps --> PROJECT urls.py
    # path('', views.simple_view, name='simple_view'),#/my_apps/simple_view --> PROJECT urls.py
    # path('sports/', views.sports_view, name='sports_view'), #/my_apps/sports/ --> PROJECT urls.py
    # path('finance/', views.finance_view, name='finance_view'), #/my_apps/finance/ --> PROJECT urls.py
    path('<str:topic>/', views.news_view, name='news_view'), #/my_apps/<topic>/ --> PROJECT urls.py
    path('<int:num1>/<int:num2>/', views.add_view, name='add_view') #/my_apps/<num1>/<num2>/ --> PROJECT urls.py
]