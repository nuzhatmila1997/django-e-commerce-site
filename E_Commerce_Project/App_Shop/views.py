from django.shortcuts import render

#default views
from django.views.generic import ListView, DetailView

#models
from App_Shop.models import Product

#mixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html' #by default nam set object_list

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html' #by default nam set object
